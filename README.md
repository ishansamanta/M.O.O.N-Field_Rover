# M.O.O.N. — Intelligent Agricultural Rover 🌱

<p align="center">
  <img src="https://github.com/ishansamanta/M.O.O.N-Field_Rover/blob/main/Inventory/6.jpeg" alt="M.O.O.N. Intelligent Agricultural Rover" width="40">
</p>

<p align="center">
  **Mobile Robotics | Artificial Intelligence | Computer Vision | Smart Agriculture**
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Smart%20India%20Hackathon-2026-blue" />
  <img src="https://img.shields.io/badge/Domain-Agriculture-green" />
  <img src="https://img.shields.io/badge/Category-Hardware-orange" />
  <img src="https://img.shields.io/badge/Team-M.O.O.N-black" />
</p>

---

## 1. Project Overview

**M.O.O.N. (Intelligent Agricultural Rover)** is a smart, four-wheel mobile agricultural monitoring system developed to improve field-level data collection and support data-driven farming decisions.

The system integrates embedded electronics, environmental sensors, camera-based image acquisition, artificial intelligence, machine learning, and cloud-based data processing into a unified agricultural platform.

The rover is designed to collect information from different locations in an agricultural field, process sensor and image data, and present meaningful agricultural insights through a dedicated web dashboard.

The primary objective is to help farmers and agricultural researchers monitor crop conditions, identify potential problems, and make more informed agricultural decisions.

### Project Information

| Parameter | Details |
|---|---|
| Project Name | M.O.O.N. |
| Full Name | Intelligent Agricultural Rover |
| Competition | Smart India Hackathon 2026 |
| Problem Statement ID | SIH26210 |
| Team ID | 177743 |
| Team Name | M.O.O.N. |
| Theme | Agriculture, Food Tech & Rural Development |
| Category | Hardware |

---

## 2. Project Vision

Our vision is to develop an intelligent agricultural rover capable of transforming conventional field inspection into an automated, sensor-driven, and AI-assisted monitoring process.

Instead of depending entirely on manual field observation, M.O.O.N. aims to collect agricultural information from multiple locations and convert it into understandable digital insights.

### One Field Scan. Four AI Insights.

- **Crop Health Analysis:** Estimation of leaf yellowness and healthy leaf area.
- **Pest Intelligence:** Pest detection and count estimation.
- **Soil Recognition:** Automated soil type classification.
- **Disease Detection:** Identification of potential plant diseases.

---

## 3. Key Features

### 3.1 Four-Wheel Rover Mobility
- Four-wheel mobile rover architecture.
- Arduino-based motor control.
- DC gear motor-driven movement.
- Motor driver-based movement control.
- Ultrasonic obstacle detection using HC-SR04.
- Designed for agricultural field monitoring.

### 3.2 Environmental Monitoring
- Temperature measurement.
- Humidity monitoring.
- Air-quality monitoring.
- Expandable sensor architecture for additional agricultural parameters.

### 3.3 Camera-Based Monitoring
- Crop and leaf image acquisition.
- Soil image collection.
- Computer vision-based image processing.
- Image-based agricultural observation.

### 3.4 AI/ML-Based Agricultural Analysis

| AI Module | Function |
|---|---|
| Crop Health Analysis | Estimates leaf yellowness and healthy leaf area |
| Pest Intelligence | Detects pests and estimates their count |
| Soil Recognition | Classifies soil types using image analysis |
| Disease Detection | Identifies potential plant diseases |

### 3.5 Cloud and Web Dashboard
- Centralized agricultural data monitoring.
- AI-generated analysis results.
- Image and sensor data visualization.
- Internet-based data transmission.
- Cloud storage and processing.
- Architecture designed for future AI model integration.

---

## 4. Hardware Architecture and Components

The rover combines embedded computing, motor control, sensors, camera-based data acquisition, and a power supply system.

### 4.1 Main Hardware Components

| Component | Purpose |
|---|---|
| Raspberry Pi 3B+ | Main processing and data acquisition |
| Arduino UNO R3 | Rover movement and hardware control |
| DC Gear Motors (4) | Four-wheel mobility |
| Motor Driver | Motor direction and speed control |
| HC-SR04 Ultrasonic Sensor | Obstacle detection |
| DHT11 Sensor | Temperature and humidity monitoring |
| MQ-135 Sensor | Air-quality monitoring |
| Camera / Webcam | Crop, leaf and soil image acquisition |
| Battery System | Power supply |
| Wi-Fi / Internet | Data communication |

### 4.2 Mechanical Rover Design

The rover uses a four-wheel chassis with individual wheel-drive arrangements. Its mechanical structure is designed to accommodate electronic components, sensing modules, and the camera system.

**Conceptual CAD Design**

![M.O.O.N. Rover CAD Model](assets/rover-cad.jpg)

**Physical Rover Platform**

![M.O.O.N. Rover Platform](assets/rover-platform-overview.jpg)

*Assembled four-wheel platform showing the mechanical structure, component placement, sensor arrangement, and electronics.*

### 4.3 Circuit and Wiring Architecture

![M.O.O.N. Circuit Diagram](assets/circuit-diagram.jpg)

*Hardware wiring and connection architecture for the rover's electronic components.*

### 4.4 Electronics Integration

![M.O.O.N. Electronics Platform](assets/electronics-platform-closeup.jpg)

*Physical electronics arrangement showing the controller boards, ultrasonic sensor, breadboards, wiring, and other electronic modules.*

The electronics architecture separates movement control from higher-level data processing, allowing modular development and future expansion.

### 4.5 Power Management and Charging

![M.O.O.N. Battery Charging Setup](assets/battery-charging-setup.jpg)

*Battery charging and power supply arrangement used during prototype development.*

The power system supplies the rover's electronic and motor-control components. Power distribution, battery management, and efficient energy consumption are important considerations for reliable field operation.

### 4.6 Downloadable 3D Model

The project also includes an OBJ-format 3D model exported from Tinkercad.

**[Download M.O.O.N. Rover 3D Model (.OBJ)](models/tinker.obj)**

The model can be used for 3D visualization, mechanical reference, and further chassis development.

---

## 5. System Architecture and Working Methodology

M.O.O.N. follows a structured workflow connecting physical rover operations with digital agricultural analysis.

### 5.1 Working Process

1. **Rover Movement:** Arduino UNO controls the four-wheel drive system through the motor driver.
2. **Obstacle Detection:** HC-SR04 detects nearby obstacles and supports movement safety.
3. **Data Acquisition:** The Raspberry Pi collects camera images and environmental sensor readings.
4. **Local Processing:** Python-based processing prepares and validates collected information.
5. **Data Transmission:** Images and sensor readings are transmitted through Wi-Fi/Internet.
6. **AI/ML Processing:** Agricultural images are analyzed using computer vision and AI/ML models.
7. **Cloud Integration:** Processed information can be stored and organized for centralized access.
8. **Dashboard Visualization:** The web dashboard presents field information and analysis results.

### 5.2 System Data Flow

```text
             AGRICULTURAL FIELD
                      |
                      v
              FOUR-WHEEL ROVER
                      |
             +--------+--------+
             |                 |
             v                 v
        CAMERA SYSTEM     ENVIRONMENTAL
                              SENSORS
             |                 |
             +--------+--------+
                      |
                      v
                RASPBERRY PI 3B+
                DATA ACQUISITION
                      |
                      v
             IMAGE / SENSOR DATA
                  PROCESSING
                      |
                      v
               WI-FI / INTERNET
                      |
                      v
                CLOUD / AI ENGINE
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
        CROP         PEST       SOIL /
       HEALTH     DETECTION    DISEASE
          |           |           |
          +-----------+-----------+
                      |
                      v
                WEB DASHBOARD
                      |
                      v
             AGRICULTURAL INSIGHTS
```

*Conceptual system architecture. Individual AI modules are progressively developed and integrated.*

### 5.3 Offline Data Handling

The proposed architecture also supports local data storage when internet connectivity is weak. Stored information can be synchronized with cloud services when connectivity becomes available.

---

## 6. AI and Computer Vision Implementation

One of the major components of M.O.O.N. is its computer vision-based agricultural analysis system.

The system processes captured leaf images to identify the leaf region, detect yellow or discolored areas, and estimate the relative proportion of healthy and affected regions.

### 6.1 Leaf Segmentation and Health Estimation

The image-processing workflow consists of:

- Input image acquisition.
- Leaf region segmentation.
- Extraction of the leaf area.
- Identification of yellow-colored regions.
- Pixel-based area calculation.
- Percentage-based health estimation.
- Visualization of detected regions.

### 6.2 Demonstration 1 — Crop Leaf Analysis

![Corn Leaf Segmentation and Analysis](assets/leaf-analysis-corn.jpg)

**Observed Analysis Results**

| Parameter | Result |
|---|---:|
| Segmented Leaf Area | 42,286 pixels |
| Yellow Region | 11,092 pixels |
| Yellow Area | 26.23% |
| Healthy Area | 73.77% |

### 6.3 Demonstration 2 — Leaf Condition Analysis

![Leaf Segmentation and Yellow Region Detection](assets/leaf-analysis-leaf.jpg)

**Observed Analysis Results**

| Parameter | Result |
|---|---:|
| Segmented Leaf Area | 115,639 pixels |
| Yellow Region | 1,893 pixels |
| Yellow Area | 1.64% |
| Healthy Area | 98.36% |

*Note: These values represent image-processing estimates from the displayed samples. They are not independently validated plant disease diagnoses.*

---

## 7. Prototype Development and Hardware Demonstration

M.O.O.N. has progressed through conceptual mechanical design, circuit planning, physical chassis development, electronics integration, and prototype testing.

The following photographs document the physical development of the rover.

### 7.1 Front View

![M.O.O.N. Rover Front View](assets/prototype-front.jpg)

### 7.2 Rear View

![M.O.O.N. Rover Rear View](assets/prototype-rear.jpg)

### 7.3 Side View

![M.O.O.N. Rover Side View](assets/prototype-side.jpg)

### 7.4 Electronics Testing

![M.O.O.N. Electronics Testing](assets/electronics-testing.jpg)

### 7.5 System Testing

![M.O.O.N. System Testing](assets/system-testing.jpg)

### 7.6 Field Testing

![M.O.O.N. Rover Field Testing](assets/field-testing.jpg)

### 7.7 Rover Demonstration

![M.O.O.N. Rover Demonstration](assets/rover-demonstration.jpg)

### 7.8 Team and Prototype

![M.O.O.N. Team with Rover](assets/team-prototype.jpg)

### 7.9 Rover Demonstration Video

The project also includes a recorded video documenting the physical rover and its demonstration.

**[▶ Watch the M.O.O.N. Rover Demonstration](media/rover-demonstration.mp4)**

---

## 8. Technology Stack

| Technology | Application |
|---|---|
| Python | Processing and system development |
| Raspberry Pi 3B+ | Embedded computing |
| Arduino UNO R3 | Hardware and motor control |
| Computer Vision | Image processing and segmentation |
| AI / Machine Learning | Agricultural analysis |
| OpenCV | Image processing |
| PyTorch | AI/ML model development |
| Wi-Fi / Internet | Communication |
| Cloud Storage | Data storage and synchronization |
| Web Technologies | Digital monitoring dashboard |

---

## 9. Feasibility, Challenges and Scalability

### 9.1 Feasibility
- Raspberry Pi-based processing.
- Arduino-based motor control.
- Camera and sensor integration.
- Modular hardware configuration.
- Cloud and AI/ML processing architecture.

### 9.2 Scalability
- Integration of additional soil sensors.
- Expansion of AI/ML models.
- Improved computer vision capabilities.
- Enhanced field data visualization.
- Future improvements in rover mobility and autonomy.

### 9.3 Challenges and Mitigation Strategies

| Challenge | Proposed Strategy |
|---|---|
| Uneven agricultural terrain | Suitable chassis and high-torque motors |
| Battery consumption | Power management and battery monitoring |
| Sensor accuracy | Sensor calibration and data filtering |
| Dust and moisture | Protective electronics enclosure |
| Poor internet connectivity | Local storage and cloud synchronization |

---

## 10. Expected Impact

M.O.O.N. aims to support agricultural modernization through accessible mobile sensing and AI-assisted field monitoring.

| Impact Area | Expected Benefit |
|---|---|
| Social | Easier and faster field monitoring |
| Economic | Reduced manual inspection effort |
| Environmental | Data-driven use of agricultural resources |
| Technical | Centralized sensor and image-based field information |
| Scalability | Expandable sensor and AI model architecture |

### Target Users

- Farmers and agricultural workers.
- Agricultural researchers.
- Field monitoring teams.
- Agri-tech service providers.

---

## 11. Future Development Roadmap

The project is designed for continuous improvement.

- [x] Initial four-wheel rover mechanical prototype.
- [x] Hardware connection and wiring design.
- [x] Arduino-based movement control architecture.
- [x] Raspberry Pi-based data acquisition architecture.
- [x] Initial camera-based leaf segmentation demonstration.
- [ ] Complete integration of environmental sensors.
- [ ] Integration of all four AI analysis modules.
- [ ] Cloud-based AI processing integration.
- [ ] Complete web dashboard integration.
- [ ] Improved autonomous field navigation.
- [ ] Extended field testing and validation.
- [ ] Additional agricultural sensor integration.

---

## 12. Project Team

**M.O.O.N. — Smart India Hackathon 2026**

We are a student innovation team working towards developing an intelligent agricultural monitoring system by combining robotics, embedded systems, artificial intelligence, and computer vision.

### Team Photograph

<p align="center">
  <img src="assets/team.jpg" alt="M.O.O.N. Project Team" width="750">
</p>

---

## 13. Research and Technical References

### Research References

- Agricultural Robotics — Annual Review: Agricultural robots, sensing, automation, and data-driven precision farming.
- A Review of Robots, Perception, and Tasks in Precision Agriculture: Mobile agricultural robots, crop/soil monitoring, and robotic perception.
- Integration of Smart Sensors and IoT in Precision Agriculture: Soil sensors, IoT-based monitoring, and data-driven agricultural decision-making.
- FAO — Precision Agriculture for Smallholder Farmers: IoT, AI, cloud computing, and digital technologies in agriculture.

### Technical References

- Raspberry Pi Official Documentation — https://www.raspberrypi.com/documentation/
- Arduino Official Documentation — https://docs.arduino.cc/
- OpenCV Documentation — https://docs.opencv.org/
- PyTorch Documentation — https://pytorch.org/docs/
- Food and Agriculture Organization — https://www.fao.org/

---

## 14. Repository Structure

```text
MOON-Agricultural-Rover/
│
├── README.md
│
├── assets/
│   ├── prototype-front.jpg
│   ├── prototype-rear.jpg
│   ├── prototype-side.jpg
│   ├── rover-cad.jpg
│   ├── rover-platform-overview.jpg
│   ├── circuit-diagram.jpg
│   ├── electronics-platform-closeup.jpg
│   ├── battery-charging-setup.jpg
│   ├── electronics-testing.jpg
│   ├── field-testing.jpg
│   ├── system-testing.jpg
│   ├── rover-demonstration.jpg
│   ├── team-prototype.jpg
│   ├── team.jpg
│   ├── leaf-analysis-corn.jpg
│   └── leaf-analysis-leaf.jpg
│
├── models/
│   └── tinker.obj
│
├── media/
│   └── rover-demonstration.mp4
│
├── arduino/
│
├── raspberry-pi/
│
├── ai-models/
│
├── dashboard/
│
└── docs/
```

*The folder structure represents the recommended repository organization. Additional folders can be populated as their respective software and documentation are published.*

---

## 15. Project Information

**Project:** M.O.O.N. — Intelligent Agricultural Rover

**Competition:** Smart India Hackathon 2026

**Problem Statement ID:** SIH26210

**Team ID:** 177743

**Team Name:** M.O.O.N.

**Theme:** Agriculture, Food Tech & Rural Development

---

<p align="center">
  <strong>M.O.O.N. — Smarter Field Monitoring. Smarter Agricultural Decisions.</strong>
  <br><br>
  <em>Engineering Technology for the Future of Agriculture.</em>
</p>
