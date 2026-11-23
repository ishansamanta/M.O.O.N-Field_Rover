# 🌙 M.O.O.N.
### Mobile Observation and Object Navigation

<p align="center">
  <strong>AN AI-POWERED AGRICULTURAL ROVER</strong>
  <br>
  <em>Intelligent Observation. Agricultural Intelligence. Robotic Mobility.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Project-M.O.O.N.-111827?style=for-the-badge&logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/AI_Models-04-2563EB?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-Raspberry_Pi-C51A4A?style=for-the-badge&logo=raspberrypi&logoColor=white" />
  <img src="https://img.shields.io/badge/Controller-Arduino-00979D?style=for-the-badge&logo=arduino&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-In_Development-orange?style=for-the-badge" />
</p>

---

## ✦ 01 — THE PROJECT

**M.O.O.N.** (Mobile Observation and Object Navigation) is a modular, AI-powered agricultural rover designed to bring artificial intelligence, robotics, and intelligent monitoring into agricultural environments.

Built around a distributed computing architecture, M.O.O.N. combines an eight-wheel robotic platform, two Raspberry Pi 3B+ computers, an Arduino Uno, and a custom web dashboard.

Its primary intelligence comes from four specialized AI models designed to analyze agricultural environments:

- Soil Detection
- Crop Detection
- Crop Disease Detection
- Pest Detection

The rover captures real-time visual information, processes it through selected AI models, and presents the results through its web dashboard.

The system is designed to allow operators to select individual models or multiple models according to their requirements.

<p align="center">
  <strong>ONE ROVER. FOUR AI MODELS. ONE INTELLIGENT AGRICULTURAL PLATFORM.</strong>
</p>

---

## ✦ 02 — AT A GLANCE

<table>
<tr>
<td align="center" width="25%">
<strong>Four AI Models</strong>
<br>
<sub>Agricultural Intelligence</sub>
</td>
<td align="center" width="25%">
<strong>Two Raspberry Pi 3B+ </strong>
<br>
<sub>Distributed Processing</sub>
</td>
<td align="center" width="25%">
<h2>08</h2>
<strong>Wheels</strong>
<br>
<sub>Mobile Platform</sub>
</td>
<td align="center" width="25%">
<h2>01</h2>
<strong>Dashboard</strong>
<br>
<sub>Central Interface</sub>
</td>
</tr>
</table>

### Core Capabilities

| Capability | Description |
|:---|:---|
| 👁️ Environmental Observation | Camera-based agricultural monitoring |
| 🧠 Artificial Intelligence | Four specialized agricultural AI models |
| 🌱 Soil Analysis | Visual soil detection and classification |
| 🌾 Crop Recognition | Crop identification and detection |
| 🦠 Disease Detection | Identification of visible crop disease symptoms |
| 🐛 Pest Detection | Identification of supported agricultural pests |
| 🎮 Remote Mobility | Web-based rover movement control |
| 🌐 Live Monitoring | Camera streaming and AI result visualization |

---

## ✦ 03 — THE FOUR INTELLIGENCE SYSTEMS

M.O.O.N. is built around four independent AI models. Each model has its own detection purpose and can be selected through the web dashboard.

<details open>
<summary><strong>01 — SOIL DETECTION</strong></summary>

### 🌱 Soil Intelligence

Analyzes visible soil characteristics through camera-based AI processing.

**Intended capabilities:**
- Soil type identification.
- Visual soil classification.
- Soil surface observation.
- Identification of visible soil characteristics.

</details>

<details open>
<summary><strong>02 — CROP DETECTION</strong></summary>

### 🌾 Crop Intelligence

Identifies and detects crops within the rover's camera feed.

**Intended capabilities:**
- Crop identification.
- Crop category recognition.
- Crop region detection.
- Visual crop observation.

</details>

<details open>
<summary><strong>03 — CROP DISEASE DETECTION</strong></summary>

### 🦠 Plant Health Intelligence

Analyzes plant images to identify visible disease symptoms.

**Intended capabilities:**
- Diseased leaf detection.
- Disease category identification.
- Visible symptom recognition.
- Healthy and affected plant classification.

</details>

<details open>
<summary><strong>04 — PEST DETECTION</strong></summary>

### 🐛 Pest Intelligence

Detects and identifies supported agricultural pests in camera images.

**Intended capabilities:**
- Insect detection.
- Pest identification.
- Pest location detection.
- Visual pest monitoring.

</details>

> **Important:** Camera-based soil detection is limited to visible characteristics. Accurate pH, moisture, NPK, and chemical measurements require dedicated sensors or laboratory testing. AI disease and pest identification is also limited to the classes represented in the respective trained models.

---

## ✦ 04 — SYSTEM ARCHITECTURE

M.O.O.N. follows a distributed architecture where every major hardware component has a dedicated responsibility.

### Hardware Architecture

| Component | Responsibility |
|:---|:---|
| Raspberry Pi 1 (3B+) | Camera acquisition, communication and dashboard connectivity |
| Raspberry Pi 2 (3B+) | Dedicated AI processing |
| Arduino Uno | Low-level motor and movement control |
| USB Webcam | Live visual input |
| Motor Drivers | Motor direction and power control |
| Custom Web Dashboard | User interface and system monitoring |

### The Distributed Architecture

```text
                     ┌───────────────┐
                     │     USER      │
                     └───────┬───────┘
                             │
                             ▼
                ┌────────────────────────┐
                │   M.O.O.N. DASHBOARD   │
                │  Camera / AI / Control │
                └───────────┬────────────┘
                            │
                            ▼
                ┌────────────────────────┐
                │   RASPBERRY PI 1       │
                │       (3B+)            │
                │                        │
                │  CAMERA & COMMUNICATION│
                └───────┬─────────┬──────┘
                        │         │
               VIDEO    │         │ MOVEMENT
                        ▼         ▼
              ┌─────────────┐  ┌─────────────┐
              │ RASPBERRY   │  │  ARDUINO    │
              │ PI 2 (3B+)  │  │   UNO       │
              │             │  └──────┬──────┘
              │ AI PROCESSING│         │
              └──────┬──────┘         ▼
                     │           ┌────────────┐
                     ▼           │   MOTOR    │
              ┌─────────────┐    │  DRIVERS   │
              │ MODEL       │    └──────┬─────┘
              │ MANAGER     │           │
              └──────┬──────┘           ▼
                     │              DC MOTORS
       ┌─────────────┼─────────────┐     │
       │             │             │     ▼
       ▼             ▼             ▼   ROVER
  ┌─────────┐   ┌─────────┐   ┌─────────┐
  │  SOIL   │   │  CROP   │   │ DISEASE │
  │  MODEL  │   │  MODEL  │   │  MODEL  │
  └────┬────┘   └────┬────┘   └────┬────┘
       │             │             │
       └─────────────┼─────────────┘
                     │
                ┌────▼────┐
                │  PEST   │
                │  MODEL  │
                └────┬────┘
                     │
                     ▼
              RESULT PROCESSING
                     │
                     ▼
               WEB DASHBOARD
```

**Architecture principle:** All four AI models are independent and parallel model branches under the same AI model manager. The diagram illustrates their logical organization, not a mandatory execution sequence. Selected models can be scheduled for inference according to available resources.

---

## ✦ 05 — AI PROCESSING ENGINE

The second Raspberry Pi 3B+ serves as the dedicated AI processing unit.

Its primary responsibility is to receive camera frames, process them using selected AI models, and return inference results.

### Processing Pipeline

```text
       USB WEBCAM
            │
            ▼
      CAMERA CAPTURE
            │
            ▼
      RASPBERRY PI 1
            │
            ▼
       FRAME TRANSFER
            │
            ▼
      RASPBERRY PI 2
            │
            ▼
     IMAGE PREPROCESSING
            │
            ▼
       MODEL MANAGER
            │
     ┌──────┼──────┬──────┐
     ▼      ▼      ▼      ▼
    SOIL   CROP  DISEASE  PEST
     │      │      │      │
     └──────┴──────┴──────┘
            │
            ▼
      RESULT PROCESSING
            │
            ▼
       WEB DASHBOARD
```

### Flexible Model Selection

The operator can select:

| Selection | Execution Configuration |
|:---|:---|
| 1 Model | Any individual model |
| 2 Models | Any two-model combination |
| 3 Models | Any three-model combination |
| 4 Models | All four models |

The model manager will coordinate model loading, selection, and execution.

### Model Deployment Options

Potential supported formats and inference technologies include:

| Technology | Application |
|:---|:---|
| TensorFlow Lite | Lightweight neural network inference |
| ONNX Runtime | Cross-framework inference |
| NCNN | Optimized neural network deployment |
| OpenCV DNN | Supported computer vision models |
| PyTorch | Model development and compatible deployment |

The final runtime will be selected according to the frameworks used to train the models.

### Optimization Strategy

The Raspberry Pi 3B+ has limited computing and memory resources. Therefore, optimization is essential.

Planned techniques include:

- INT8 quantization.
- Lightweight model architectures.
- Reduced input resolution.
- Frame skipping.
- Efficient image preprocessing.
- Model loading and unloading.
- Sequential inference when necessary.
- Resource-aware execution scheduling.

Selecting four models does not automatically mean all four can run simultaneously at real-time speed.

---

## ✦ 06 — MECHANICAL DESIGN

### Eight-Wheel Robotic Platform

M.O.O.N. is planned around an eight-wheel mechanical configuration designed to support a mobile agricultural platform.

**Proposed configuration:**

- 8 total wheels.
- 4 common axle assemblies.
- 2 adjacent wheels per axle.
- 4 motor-driven axle positions.
- Supporting structural chassis.

### Wheel Arrangement

Each common axle is intended to connect two wheels positioned side by side, similar to the dual-wheel arrangement used in heavy vehicles.

### Chassis Structure

The proposed chassis incorporates four perpendicular straight structural rods or support members to hold the axle assemblies.

The mechanical design aims to provide:

- Structural stability.
- Weight distribution.
- Reliable axle alignment.
- Motor mounting positions.
- Electronic component mounting.
- Space for batteries and computing hardware.

The final mechanical dimensions, material selection, suspension arrangements, and drivetrain specifications will be determined during prototyping.

---

## ✦ 07 — HARDWARE SPECIFICATIONS

| Hardware | Quantity | Role |
|:---|:---:|:---|
| Raspberry Pi 3B+ | 2 | Camera and AI processing |
| Arduino Uno | 1 | Rover movement |
| USB Webcam | 1 | Visual observation |
| DC Gear Motors | 4 planned | Propulsion |
| Wheels | 8 planned | Mobility |
| Common Axles | 4 planned | Wheel connection |
| Motor Drivers | As required | Motor control |
| Chassis | 1 | Mechanical support |
| Battery System | As required | Power supply |
| Wiring | As required | Electrical connections |

*Specifications are subject to change during hardware testing.*

---

## ✦ 08 — WEB DASHBOARD

The M.O.O.N. web dashboard is the central interface through which the operator interacts with the rover.

Rather than depending entirely on an external robotics interface, M.O.O.N. is designed around its own custom dashboard.

### Dashboard Modules

| Interface | Function |
|:---|:---|
| 📷 Live Camera | View the rover's camera feed |
| 🎮 Rover Control | Control movement remotely |
| 🌱 Soil Detection | View soil analysis results |
| 🌾 Crop Detection | View crop identification |
| 🦠 Disease Detection | View crop disease results |
| 🐛 Pest Detection | View pest identification |
| 🧠 AI Model Manager | Select individual or multiple models |
| 📊 System Monitoring | Monitor device and connection status |

### Dashboard Workflow

```text
       M.O.O.N. DASHBOARD
               │
       ┌───────┴────────┐
       │                │
       ▼                ▼
   AI CONTROL       ROVER CONTROL
       │                │
       ▼                ▼
  RASPBERRY PI 2    RASPBERRY PI 1
       │                │
       ▼                ▼
  FOUR AI MODELS     ARDUINO UNO
       │                │
       ▼                ▼
  AI RESULTS         MOTOR CONTROL
       │                │
       ▼                ▼
  DASHBOARD            ROVER
```

Potential communication technologies include HTTP APIs and WebSockets, depending on the final implementation.

---

## ✦ 09 — LIVE OPERATING WORKFLOW

The intended live operating sequence is:

**01 — Initialization**

The Raspberry Pi units and Arduino Uno start, and the communication system is initialized.

**02 — Camera Acquisition**

The USB webcam connected to Raspberry Pi 1 begins capturing live footage.

**03 — Live Streaming**

Raspberry Pi 1 provides the camera feed to the dashboard.

**04 — AI Frame Transfer**

Selected camera frames are transmitted to Raspberry Pi 2.

**05 — Model Selection**

The operator selects one or more of the four agricultural AI models.

**06 — AI Inference**

Raspberry Pi 2 processes the frames using the selected models.

**07 — Result Transmission**

AI inference results are returned to the web dashboard.

**08 — Rover Movement**

Movement commands from the dashboard are forwarded through Raspberry Pi 1 to Arduino Uno.

**09 — Continuous Operation**

Camera observation, AI inference, result visualization, and manual movement can operate together according to available system resources.

---

## ✦ 10 — SOFTWARE ECOSYSTEM

The project may use the following technologies:

| Technology | Purpose |
|:---|:---|
| Python | Raspberry Pi software and AI processing |
| C/C++ | Arduino programming |
| Arduino IDE | Embedded development |
| OpenCV | Image processing |
| TensorFlow Lite | Lightweight inference |
| ONNX Runtime | AI model deployment |
| NCNN | Optimized inference |
| HTML | Dashboard structure |
| CSS | Dashboard design |
| JavaScript | Dashboard functionality |
| WebSockets | Real-time communication |
| Raspberry Pi OS | Raspberry Pi environment |
| Git / GitHub | Version control |

These are intended technology options, not a claim that every component has already been implemented.

---

## ✦ 11 — DEVELOPMENT ROADMAP

M.O.O.N. is being developed through six major stages.

### PHASE 01 — MECHANICAL ENGINEERING
- [ ] Finalize chassis design.
- [ ] Develop eight-wheel configuration.
- [ ] Design four common axle assemblies.
- [ ] Mount motors and wheels.
- [ ] Test mechanical stability.

### PHASE 02 — ELECTRONICS & MOVEMENT
- [ ] Configure Arduino Uno.
- [ ] Integrate motor drivers.
- [ ] Connect DC motors.
- [ ] Implement movement commands.
- [ ] Test all movement directions.
- [ ] Implement emergency stop.

### PHASE 03 — CAMERA & COMPUTING
- [ ] Configure Raspberry Pi 1.
- [ ] Connect USB webcam.
- [ ] Implement live camera capture.
- [ ] Configure Raspberry Pi 2.
- [ ] Establish Pi-to-Pi communication.
- [ ] Implement frame transmission.

### PHASE 04 — ARTIFICIAL INTELLIGENCE
- [ ] Prepare Soil Detection Model.
- [ ] Prepare Crop Detection Model.
- [ ] Prepare Crop Disease Detection Model.
- [ ] Prepare Pest Detection Model.
- [ ] Test model compatibility.
- [ ] Optimize model formats.
- [ ] Develop model manager.
- [ ] Implement multi-model selection.
- [ ] Optimize inference performance.

### PHASE 05 — DASHBOARD INTEGRATION
- [ ] Connect dashboard to Raspberry Pi.
- [ ] Implement live camera streaming.
- [ ] Implement rover movement controls.
- [ ] Develop four-model selection interface.
- [ ] Integrate all AI results.
- [ ] Implement system monitoring.

### PHASE 06 — SYSTEM INTEGRATION
- [ ] Integrate all hardware.
- [ ] Test camera and AI operation.
- [ ] Test multiple-model execution.
- [ ] Test movement during AI processing.
- [ ] Measure processing latency.
- [ ] Optimize communication.
- [ ] Perform complete rover testing.

---

## ✦ 12 — FUTURE DEVELOPMENT

M.O.O.N. is designed to be expandable beyond its initial agricultural monitoring capabilities.

### Advanced Agricultural Monitoring
- Soil moisture sensors.
- Soil pH measurement.
- NPK measurement.
- Temperature and humidity monitoring.
- Environmental sensing.
- Crop growth observation.

### Advanced Robotics
- Autonomous navigation.
- Obstacle avoidance.
- GPS integration.
- LiDAR integration.
- SLAM-based mapping.
- Intelligent path planning.
- Automated field navigation.

### Advanced Artificial Intelligence
- Weed detection.
- Fruit detection.
- Plant counting.
- Crop health monitoring.
- Disease severity estimation.
- Pest population estimation.
- AI-assisted agricultural recommendations.

### Cloud Integration
- Cloud-based AI inference.
- Remote model management.
- Historical detection records.
- Agricultural data visualization.
- Remote rover access.
- Mission monitoring.

*These are potential future extensions and are not represented as currently implemented features.*

---

## ✦ 13 — PROJECT STATUS

<p align="center">
  <img src="https://img.shields.io/badge/Development-Planning_&_Prototyping-orange?style=for-the-badge" />
</p>

| Module | Status |
|:---|:---|
| System Architecture | Planning |
| Eight-Wheel Mechanical Design | Proposed |
| Camera Raspberry Pi | Planned |
| AI Processing Raspberry Pi | Planned |
| Arduino Movement Control | Planned |
| Soil Detection | Integration Planned |
| Crop Detection | Integration Planned |
| Crop Disease Detection | Integration Planned |
| Pest Detection | Integration Planned |
| Multi-Model Execution | Planned |
| Web Dashboard | Integration Planned |
| Complete System | Pending |

---

## ✦ 14 — REPOSITORY STRUCTURE

```text
M.O.O.N/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── hardware/
│   ├── mechanical/
│   │   ├── chassis/
│   │   ├── axle-design/
│   │   └── wheel-assembly/
│   │
│   ├── electronics/
│   │   ├── circuit-diagrams/
│   │   └── wiring/
│   │
│   └── components.md
│
├── raspberry-pi/
│   ├── camera-unit/
│   │   ├── camera.py
│   │   ├── streaming.py
│   │   └── communication.py
│   │
│   └── ai-unit/
│       ├── model-manager/
│       ├── inference/
│       ├── preprocessing/
│       └── result-processing/
│
├── arduino/
│   ├── rover-control/
│   └── motor-control/
│
├── ai-models/
│   ├── soil-detection/
│   ├── crop-detection/
│   ├── crop-disease-detection/
│   └── pest-detection/
│
├── dashboard/
│   ├── frontend/
│   └── backend/
│
├── communication/
│
├── documentation/
│   ├── architecture.md
│   ├── setup-guide.md
│   ├── hardware-guide.md
│   └── development-log.md
│
└── assets/
    ├── images/
    ├── diagrams/
    └── videos/
```

Large trained AI model files should preferably be stored using Git LFS or external model storage where appropriate.

---

## ✦ 15 — CONTRIBUTING

M.O.O.N. welcomes contributions, ideas, technical discussions, and improvements.

Potential contribution areas include:

- Robotics and mechanical engineering.
- Embedded systems.
- Artificial intelligence.
- Machine learning.
- Computer vision.
- Agricultural technology.
- Raspberry Pi development.
- Arduino programming.
- Web development.
- System architecture.

### Contribution Guidelines

1. Fork the repository.
2. Create a new branch.
3. Implement your changes.
4. Test your modifications.
5. Submit a pull request.

All contributions should aim to improve the reliability, functionality, and scalability of M.O.O.N.

---

## ✦ 16 — LICENSE

The licensing terms for M.O.O.N. will be specified by the project maintainers.

Until a license is added to the repository, all rights are reserved by the respective copyright holder.

---

<p align="center">
  <br>
  <strong>🌙 M.O.O.N.</strong>
  <br>
  <em>Mobile Observation and Object Navigation</em>
  <br><br>
  <strong>ONE ROVER. FOUR AI MODELS. SMARTER AGRICULTURAL OBSERVATION.</strong>
  <br><br>
  <sub>Building M.O.O.N., one module at a time.</sub>
</p>
