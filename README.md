# 🌱 M.O.O.N. — Intelligent Agricultural Rover

### Smart Field Monitoring • AI-Powered Crop Analysis • Precision Agriculture

<p align="center">
  <strong>One Field Scan. Four AI Insights. Smarter Farming.</strong>
</p>

<p align="center">
  An intelligent agricultural rover designed to combine mobile sensing, computer vision, AI/ML analysis and digital monitoring to support data-driven farming.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Smart%20India%20Hackathon-2026-blue?style=for-the-badge" alt="Smart India Hackathon 2026">
  <img src="https://img.shields.io/badge/Domain-Agriculture%20%26%20AgriTech-2E8B57?style=for-the-badge" alt="Agriculture and AgriTech">
  <img src="https://img.shields.io/badge/Category-Hardware-orange?style=for-the-badge" alt="Hardware">
  <img src="https://img.shields.io/badge/Project-Research%20%26%20Development-purple?style=for-the-badge" alt="Research and Development">
</p>

---

## 📌 Project Overview

**M.O.O.N. (Intelligent Agricultural Rover)** is a hardware-oriented agricultural technology project developed to improve field-level monitoring through robotics, sensors, image processing and artificial intelligence.

The project aims to develop a mobile four-wheel rover capable of collecting agricultural observations from different locations within a field. Its proposed system combines camera-based image acquisition, environmental sensing, AI-powered analysis and a centralized web dashboard.

Instead of relying entirely on manual field inspection, M.O.O.N. aims to provide farmers and agricultural researchers with organized information about crop conditions, pests, soil types and potential plant diseases.

The system is designed with a modular architecture so that additional sensors, AI models and monitoring capabilities can be integrated as development progresses.

## 🏆 Smart India Hackathon 2026

| Particular | Details |
|---|---|
| Team Name | M.O.O.N |
| Team ID | 177743 |
| Problem Statement ID | SIH26210 |
| Problem Statement | Student Innovation – Developing solutions to enhance India's agricultural primary sector and manage and process agricultural produce |
| Theme | Agriculture, Food Tech & Rural Development |
| Category | Hardware |
| Project | M.O.O.N. — Intelligent Agricultural Rover |

## 🎯 Problem Statement

Agricultural field monitoring often requires repeated manual inspections to identify crop-health issues, pest activity, soil variations and changing environmental conditions.

These inspections can be time-consuming and may not provide consistent observations across large agricultural areas.

M.O.O.N. aims to address these challenges through a mobile agricultural platform that can collect field data, process visual and sensor observations, and present useful analytical information through a digital interface.

## 💡 Proposed Solution

M.O.O.N. combines four major capabilities:

1. **Mobile Robotics:** A four-wheel rover platform for movement and field-level data collection.
2. **Environmental Monitoring:** Sensors for collecting temperature, humidity and air-quality observations, with scope for additional agricultural sensors.
3. **Computer Vision and AI:** Image-based analysis for crop health, pest detection, soil classification and potential disease identification.
4. **Digital Monitoring:** A web dashboard intended to display collected observations and AI-generated results.

The objective is to turn field observations into understandable information that can support agricultural decision-making.

## 🤖 Core AI/ML Modules

The proposed AI and computer-vision engine consists of four primary analysis modules.

| Module | Function |
|---|---|
| 🌿 Crop Health Analysis | Estimates leaf yellowness and healthy-area percentages through image segmentation and analysis |
| 🐛 Pest Intelligence | Detects pests and estimates their count from images |
| 🌱 Soil Recognition | Classifies soil types using image-based recognition |
| 🍃 Plant Disease Detection | Identifies potential plant diseases from crop images |

### AI Development and Demonstrations

The team has worked with agricultural datasets, including Kaggle datasets, and has trained and tested models using Google Colab.

Demonstration work includes:

- Soil recognition with detected soil regions and classification labels.
- Pest detection using image-based object recognition.
- Leaf segmentation and yellow-region analysis.
- Crop-health estimation using the proportion of yellow and healthy leaf areas.

The displayed analysis results represent individual model demonstrations and should not be interpreted as universal agricultural measurements.

## 🖥️ System Architecture

The project follows a modular hardware and software architecture.

### Hardware Layer

- Raspberry Pi 3B+ — primary edge-computing platform.
- Arduino UNO R3 — microcontroller for movement and hardware control.
- Four-wheel rover chassis.
- DC gear motors and motor drivers.
- Camera module for crop and soil image acquisition.
- DHT11 temperature and humidity sensor.
- MQ-135 air-quality sensor.
- HC-SR04 ultrasonic sensor for obstacle detection.
- Additional agricultural sensors as the platform develops.

### Software and AI Layer

- Python-based processing.
- Computer vision and image analysis.
- AI/ML model integration.
- Local data processing and storage.
- Wi-Fi and Internet connectivity.
- Cloud-based processing and storage.
- Web-based monitoring dashboard.

### Conceptual Data Flow

```text
          AGRICULTURAL FIELD
                  |
                  v
       +----------------------+
       |  FOUR-WHEEL ROVER    |
       |  Mobility & Control  |
       +----------------------+
                  |
          +-------+-------+
          |               |
          v               v
    +-----------+   +-------------+
    |  CAMERA   |   |   SENSORS   |
    | Crop/Soil |   | Environment |
    |  Images   |   |  & Obstacles|
    +-----------+   +-------------+
          |               |
          +-------+-------+
                  |
                  v
       +----------------------+
       | RASPBERRY PI 3B+     |
       | Data Collection      |
       | Local Processing     |
       +----------------------+
                  |
                  v
       +----------------------+
       | AI / ML PROCESSING   |
       | Crop Health          |
       | Pest Detection       |
       | Soil Classification |
       | Disease Detection    |
       +----------------------+
                  |
                  v
       +----------------------+
       | CLOUD / DATA STORAGE |
       +----------------------+
                  |
                  v
       +----------------------+
       | M.O.O.N. WEB DASHBOARD|
       | Monitoring & Results |
       +----------------------+
```

*This diagram represents the proposed system workflow. Individual hardware, software and AI components are being developed and integrated progressively.*

## ⚙️ Methodology

The proposed operational workflow is divided into seven stages.

**1. Rover Movement**

The four-wheel rover moves through the agricultural field using its motor-control system. Obstacle detection is intended to use the HC-SR04 ultrasonic sensor.

**2. Data Acquisition**

The camera captures crop and soil images while connected sensors collect environmental observations.

**3. Local Processing**

The Raspberry Pi collects incoming data, performs basic filtering and prepares information for further processing.

**4. Data Transmission**

Collected images and sensor readings can be transmitted through Wi-Fi or Internet connectivity. Local storage is intended to support later synchronization when connectivity is weak.

**5. AI/ML Analysis**

Agricultural images are processed using the relevant AI models to identify crop-health conditions, pests, soil types and potential diseases.

**6. Result Generation**

The analysis is converted into structured information that can help identify field conditions and potential problem areas.

**7. Dashboard Visualization**

The web dashboard is intended to provide a centralized interface for monitoring field observations and viewing analysis results.

## 🛠️ Technologies and Components

| Category | Technologies / Components |
|---|---|
| Edge Computing | Raspberry Pi 3B+ |
| Microcontroller | Arduino UNO R3 |
| Programming | Python, Arduino C/C++ |
| Computer Vision | OpenCV |
| AI/ML | Trained image-analysis and detection models |
| Sensors | DHT11, MQ-135, HC-SR04 |
| Mobility | Four DC gear motors, motor drivers and four-wheel chassis |
| Connectivity | Wi-Fi / Internet |
| Data Management | Local storage and cloud storage |
| User Interface | Custom web dashboard |

## 🚜 Rover Prototype and Development

The physical rover is being developed as a four-wheel mobile agricultural platform.

The prototype development process includes:

- Mechanical chassis construction.
- Four-wheel mobility arrangement.
- Motor and controller integration.
- Camera and sensor mounting.
- Electronic wiring and circuit development.
- Arduino-based movement and servo-control programming.
- Physical testing and mechanical restructuring.

Initial prototype testing helped identify structural and stability-related issues. These observations are being used to improve the mechanical design and prepare a more stable platform.

The project is being developed incrementally, with mechanical, electronic and AI components integrated as they become ready.

## 🧪 AI Demonstration Results

The following examples illustrate the type of image analysis being explored by the team.

### Soil Recognition

The soil-analysis demonstration identifies regions labelled as red soil and black soil within an agricultural field image.

### Leaf Health and Yellow-Region Analysis

The leaf-analysis demonstrations use segmentation to isolate leaf regions and estimate yellow areas.

Example results shown in the team's demonstrations:

| Demonstration | Yellow Area | Healthy Area |
|---|---:|---:|
| Leaf Analysis 1 | 1.64% | 98.36% |
| Leaf Analysis 2 | 26.23% | 73.77% |

These are example outputs from individual images, not validated field-wide crop-health measurements.

### Pest Detection

The pest-detection module is being explored through image-based AI models to identify and estimate pest counts.

## 🌍 Impact and Benefits

### Social Impact
- Supports easier agricultural field monitoring.
- Provides organized information for farmers and agricultural workers.
- Helps agricultural researchers collect field observations.

### Economic Impact
- Aims to reduce repeated manual inspection effort.
- Supports more informed resource-management decisions.
- Provides a platform for further agricultural automation.

### Environmental Impact
- Encourages data-driven agricultural monitoring.
- Supports the potential for more informed water and fertilizer management.
- Helps identify field conditions that may require attention.

### Technical Impact
- Integrates robotics, sensors, computer vision and AI.
- Provides a modular platform for additional sensors and models.
- Establishes a foundation for intelligent agricultural monitoring.

## ⚠️ Challenges and Risk Management

| Challenge | Proposed Strategy |
|---|---|
| Uneven agricultural terrain | Improve chassis design and use suitable high-torque motors |
| Battery consumption | Power management and battery monitoring |
| Sensor accuracy | Calibration and data filtering |
| Dust and moisture | Protective electronics enclosure |
| Poor rural connectivity | Local storage and later cloud synchronization |
| Limited edge-computing resources | Model optimization and efficient processing |

## 📈 Development Roadmap

The project is being developed through progressive integration.

- [x] Initial four-wheel rover prototype development.
- [x] Initial electronics and controller integration.
- [x] Arduino-based movement and servo-control development.
- [x] Agricultural AI model experimentation and testing.
- [x] Initial soil and leaf-analysis demonstrations.
- [ ] Mechanical stability improvements.
- [ ] Complete camera and sensor integration.
- [ ] Optimize AI models for available computing hardware.
- [ ] Integrate selected AI models into the rover workflow.
- [ ] Connect the rover to the custom web dashboard.
- [ ] Develop reliable data transmission and storage.
- [ ] Conduct integrated agricultural field testing.
- [ ] Improve system reliability and scalability.

*Checklist items reflect the development information currently documented by the team and can be updated as work progresses.*

## 👥 Team M.O.O.N.

M.O.O.N. is being developed through collaborative work across mechanical design, electronics, embedded programming, AI/ML experimentation and software integration.

The team focuses on combining hardware engineering and intelligent software to develop a practical agricultural monitoring platform.

## 📂 Repository Structure

```text
M.O.O.N-Field_Rover/
│
├── Inventory/
│   ├── Prototype photographs
│   ├── AI demonstration images
│   ├── Rover demonstration videos
│   ├── Inventory & Work Logs
│   ├── Official SIH project document
│   ├── rover_locomotion_demo.ino
│   └── tinker.obj
│
├── README.md
│
└── [Additional source code and project modules]
```

The `Inventory/` directory contains project documentation, prototype media, development records and technical resources. Browse the folder to explore the available files.

## 📸 Project Gallery

The repository's Inventory folder contains photographs and other media documenting rover construction, hardware arrangements, team development activities and AI demonstrations.

**[View All Project Photographs and Media →](Inventory/)**

**[View Development Work Logs →](Inventory/Inventory%20%26%20Work%20Logs)**

**[View the Official SIH 2026 Project Document →](Inventory/MOO N_SIH2026_Official_Template_Fitted_Final90.pdf)**

## 📚 Research and Technical References

The project draws on the following areas of research and technical documentation:

- Agricultural robotics and precision farming.
- Robots, perception and tasks in precision agriculture.
- Smart sensors and IoT integration in agriculture.
- FAO resources on precision agriculture for smallholder farmers.
- Raspberry Pi official documentation.
- Arduino UNO documentation.
- OpenCV documentation.
- PyTorch documentation.

## 🔮 Future Scope

Potential future development directions include:

- Integration of additional soil-monitoring sensors.
- Improved crop-health and disease-analysis models.
- More efficient AI inference on edge hardware.
- Expanded field-level data collection.
- Better mechanical stability and mobility.
- Improved dashboard visualizations.
- Historical field-data analysis and reporting.
- More reliable offline operation and cloud synchronization.

These are intended development directions rather than claims of currently completed functionality.

## 🤝 Collaboration

M.O.O.N. is an ongoing research and development project focused on intelligent agricultural field monitoring.

We welcome technical discussions, ideas and collaboration related to:

- Agricultural robotics.
- Embedded systems and electronics.
- Computer vision and AI/ML.
- Precision agriculture.
- Edge computing and cloud integration.
- Agricultural data visualization.

## 📄 Project Documentation

- **Repository:** [M.O.O.N. Field Rover](https://github.com/ishansamanta/M.O.O.N-Field_Rover)
- **Project Media:** [Inventory Folder](Inventory/)
- **Technical Code:** [Arduino Locomotion Demo](Inventory/rover_locomotion_demo.ino)
- **3D Model:** [Rover OBJ Model](Inventory/tinker.obj)

---

<p align="center">
  <strong>M.O.O.N. — Intelligent Agricultural Rover</strong>
  <br>
  <em>Engineering a smarter approach to agricultural field monitoring.</em>
  <br><br>
  <strong>SMART INDIA HACKATHON 2026</strong>
</p>
