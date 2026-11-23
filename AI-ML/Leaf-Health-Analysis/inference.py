
import os
import cv2
import torch
import argparse
import numpy as np

from PIL import Image
from sam2.build_sam import build_sam2
from sam2.automatic_mask_generator import SAM2AutomaticMaskGenerator


# ============================================================
# 1. CONFIGURATION
# ============================================================

SAM2_CHECKPOINT = "models/sam2.1_hiera_small.pt"
SAM2_CONFIG = "configs/sam2.1/sam2.1_hiera_s.yaml"

YELLOW_SATURATION_THRESHOLD = 90
YELLOW_VALUE_THRESHOLD = 100

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


# ============================================================
# 2. LOAD SAM 2.1 MODEL
# ============================================================

def load_model():

    if not os.path.exists(SAM2_CHECKPOINT):
        raise FileNotFoundError(
            f"SAM2 checkpoint not found: {SAM2_CHECKPOINT}"
        )

    model = build_sam2(
        SAM2_CONFIG,
        SAM2_CHECKPOINT,
        device=DEVICE
    )

    mask_generator = SAM2AutomaticMaskGenerator(
        model=model,
        points_per_side=8,
        points_per_batch=16,
        pred_iou_thresh=0.70,
        stability_score_thresh=0.85,
        min_mask_region_area=300
    )

    return mask_generator


# ============================================================
# 3. LEAF HEALTH ANALYSIS
# ============================================================

def predict_leaf_health(image_path, output_path="leaf_analysis.jpg"):

    if not os.path.exists(image_path):
        raise FileNotFoundError(
            f"Input image not found: {image_path}"
        )

    # Load image in RGB format
    image = Image.open(image_path).convert("RGB")
    image_rgb = np.array(image)

    height, width = image_rgb.shape[:2]
    image_area = height * width

    print(f"Image loaded: {width} x {height}")

    # --------------------------------------------------------
    # Generate SAM segmentation masks
    # --------------------------------------------------------

    mask_generator = load_model()

    print("Generating SAM 2.1 segmentation masks...")

    with torch.inference_mode():
        masks = mask_generator.generate(image_rgb)

    print(f"Total masks detected: {len(masks)}")

    if not masks:
        raise RuntimeError("SAM2 did not generate any masks.")

    # --------------------------------------------------------
    # Select the main leaf mask
    # --------------------------------------------------------

    valid_masks = []

    for index, mask_data in enumerate(masks):

        mask = mask_data["segmentation"].astype(bool)
        area = int(mask.sum())
        area_ratio = area / image_area

        if 0.015 <= area_ratio <= 0.75:
            valid_masks.append((index, mask, area))

    if not valid_masks:

        print("No mask met the area thresholds. Using largest mask.")

        valid_masks = [
            (
                index,
                item["segmentation"].astype(bool),
                int(item["segmentation"].sum())
            )
            for index, item in enumerate(masks)
        ]

    valid_masks.sort(
        key=lambda item: item[2],
        reverse=True
    )

    selected_index, leaf_mask, leaf_area = valid_masks[0]

    print(f"Selected leaf mask: {selected_index}")
    print(f"Leaf area: {leaf_area:,} pixels")

    # --------------------------------------------------------
    # Yellow region detection using HSV
    # --------------------------------------------------------

    hsv = cv2.cvtColor(
        image_rgb,
        cv2.COLOR_RGB2HSV
    )

    H, S, V = cv2.split(hsv)

    yellow_mask = (
        (H >= 18) &
        (H <= 40) &
        (S >= YELLOW_SATURATION_THRESHOLD) &
        (V >= YELLOW_VALUE_THRESHOLD) &
        leaf_mask
    )

    yellow_area = int(yellow_mask.sum())

    yellow_percentage = (
        yellow_area / leaf_area
    ) * 100.0

    healthy_percentage = 100.0 - yellow_percentage

    # --------------------------------------------------------
    # Generate visualisation
    # --------------------------------------------------------

    leaf_overlay = image_rgb.copy()

    leaf_overlay[leaf_mask] = (
        0.60 * leaf_overlay[leaf_mask] +
        0.40 * np.array([0, 255, 0])
    ).astype(np.uint8)

    final_visual = image_rgb.copy()

    # Darken non-leaf regions
    final_visual[~leaf_mask] = (
        final_visual[~leaf_mask] * 0.40
    ).astype(np.uint8)

    # Highlight yellow regions
    yellow_color = np.array([255, 220, 0])

    final_visual[yellow_mask] = (
        0.30 * final_visual[yellow_mask] +
        0.70 * yellow_color
    ).astype(np.uint8)

    # --------------------------------------------------------
    # Display and save results
    # --------------------------------------------------------

    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    axes[0].imshow(image_rgb)
    axes[0].set_title("Original Input Image")
    axes[0].axis("off")

    axes[1].imshow(leaf_overlay)
    axes[1].set_title(
        f"Leaf Segmentation\nArea: {leaf_area:,} px"
    )
    axes[1].axis("off")

    axes[2].imshow(final_visual)
    axes[2].set_title(
        f"Yellowing: {yellow_percentage:.2f}%\n"
        f"Healthy: {healthy_percentage:.2f}%"
    )
    axes[2].axis("off")

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.show()

    print("\n========== LEAF HEALTH ANALYSIS ==========")
    print(f"Yellow Area      : {yellow_area:,} pixels")
    print(f"Yellowing        : {yellow_percentage:.2f}%")
    print(f"Healthy Area     : {leaf_area - yellow_area:,} pixels")
    print(f"Healthy          : {healthy_percentage:.2f}%")
    print(f"Output saved     : {output_path}")
    print("==========================================")

    return {
        "yellow_area": yellow_area,
        "yellow_percentage": yellow_percentage,
        "healthy_percentage": healthy_percentage,
        "leaf_area": leaf_area,
        "output_path": output_path
    }


# ============================================================
# 4. RUN INFERENCE
# ============================================================

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="MOON AgriTech Leaf Health Analysis"
    )

    parser.add_argument(
        "--image",
        required=True,
        help="Path to the input leaf image"
    )

    parser.add_argument(
        "--output",
        default="leaf_analysis.jpg",
        help="Path to save the analysis image"
    )

    args = parser.parse_args()

    predict_leaf_health(
        args.image,
        args.output
    )
