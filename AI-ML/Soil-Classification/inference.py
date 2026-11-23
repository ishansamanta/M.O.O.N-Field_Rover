
import os
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
from huggingface_hub import hf_hub_download
import argparse

# ==========================================
# 1. DEVICE
# ==========================================

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

# ==========================================
# 2. MODEL PATH
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(MODEL_DIR, exist_ok=True)

MODEL_PATH = os.path.join(
    MODEL_DIR, "soil_type_model.pth"
)

# Download checkpoint if not available locally
if not os.path.exists(MODEL_PATH):

    MODEL_PATH = hf_hub_download(
        repo_id="watermelon-elite/aaagriculture-models",
        filename="soil_type_model.pth",
        local_dir=MODEL_DIR
    )

# ==========================================
# 3. LOAD CHECKPOINT
# ==========================================

try:
    checkpoint = torch.load(
        MODEL_PATH,
        map_location=DEVICE,
        weights_only=True
    )
except TypeError:
    checkpoint = torch.load(
        MODEL_PATH,
        map_location=DEVICE
    )

SOIL_CLASSES = checkpoint["class_names"]

# ==========================================
# 4. RESNET18 MODEL ARCHITECTURE
# ==========================================

backbone = models.resnet18(weights=None)

backbone.fc = nn.Sequential(
    nn.Identity(),
    nn.Linear(512, 256),
    nn.ReLU(),
    nn.Dropout(p=0.5),
    nn.Linear(256, 6)
)

class SoilClassifier(nn.Module):

    def __init__(self, backbone):
        super().__init__()
        self.backbone = backbone

    def forward(self, x):
        return self.backbone(x)


soil_model = SoilClassifier(backbone)

soil_model.load_state_dict(
    checkpoint["model_state_dict"]
)

soil_model = soil_model.to(DEVICE)
soil_model.eval()

# ==========================================
# 5. IMAGE PREPROCESSING
# ==========================================

# PROVISIONAL preprocessing.
# Verify against the original training transform
# before using this for final deployment.

soil_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# ==========================================
# 6. SOIL CLASSIFICATION
# ==========================================

def predict_soil(image_path):

    image = Image.open(image_path).convert("RGB")

    input_tensor = soil_transform(image)
    input_tensor = input_tensor.unsqueeze(0).to(DEVICE)

    with torch.no_grad():

        output = soil_model(input_tensor)

        probabilities = torch.softmax(output, dim=1)

        confidence, predicted_index = torch.max(
            probabilities, dim=1
        )

    soil_name = SOIL_CLASSES[predicted_index.item()]

    confidence_score = confidence.item() * 100

    return {
        "soil_type": soil_name,
        "confidence": round(confidence_score, 2)
    }

# ==========================================
# 7. MAIN FUNCTION
# ==========================================

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Soil Classification using ResNet18"
    )

    parser.add_argument(
        "--image",
        required=True,
        help="Path to soil image"
    )

    args = parser.parse_args()

    result = predict_soil(args.image)

    print("\n========== SOIL CLASSIFICATION ==========")
    print("Predicted Soil:", result["soil_type"])
    print("Confidence:", str(result["confidence"]) + "%")
    print("=========================================")

