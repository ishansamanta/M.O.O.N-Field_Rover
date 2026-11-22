# M.O.O.N. — Intelligent Agricultural Field Rover

<p align="center">
  <strong>Mobile Robotics · Field Sensing · Soil Sampling · AI-Assisted Precision Agriculture</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Project-M.O.O.N-245B45?style=for-the-badge" alt="M.O.O.N.">
  <img src="https://img.shields.io/badge/Platform-Raspberry%20Pi%203B%2B-C51A4A?style=for-the-badge" alt="Raspberry Pi 3B+">
  <img src="https://img.shields.io/badge/Controller-Arduino%20UNO-00979D?style=for-the-badge" alt="Arduino UNO">
  <img src="https://img.shields.io/badge/Domain-Agricultural%20Robotics-4B8B3B?style=for-the-badge" alt="Agricultural Robotics">
  <img src="https://img.shields.io/badge/SIH-2026-315A9B?style=for-the-badge" alt="Smart India Hackathon 2026">
</p>

<p align="center"><em>A modular field rover designed to bring mobile sensing, soil interaction and intelligent agricultural analysis closer to the field.</em></p>

---

## 1. Project Overview

**M.O.O.N. (Intelligent Agricultural Field Rover)** is an agricultural robotics project developed as a mobile platform for field observation, sensing and AI-assisted analysis. The system combines a four-wheel rover structure, embedded motor control, camera positioning, soil-interaction mechanisms and a Raspberry Pi-based edge-computing platform.

The project is being developed to support agricultural workflows such as crop and pest observation, plant-disease analysis, soil classification and soil sampling. Its modular design separates low-level motion and actuator control from higher-level image processing and application development.

M.O.O.N. is an active development project. This README distinguishes hardware and functions documented in the repository from capabilities that are still being integrated or validated.

## 2. Project Information

| Item | Details |
|---|---|
| Project | M.O.O.N. — Intelligent Agricultural Field Rover |
| Team | M.O.O.N. |
| Team ID | 177743 |
| Problem Statement ID | SIH26210 |
| Programme | Smart India Hackathon 2026 |
| Theme | Agriculture, Food Technology & Rural Development |
| Category | Hardware |
| Rover footprint | Approximately 2 ft × 2 ft (as recorded in the work log) |
| Edge-computing platform | Raspberry Pi 3B+ |
| Motion and actuator controller | Arduino UNO |
| Motor driver architecture | BTS7960-based left and right drive channels |

## 3. Design Objectives

- Develop a mobile four-wheel platform for agricultural field observation.
- Provide controlled rover movement and camera/sensor positioning.
- Support soil interaction through dedicated drill and NPK actuator mechanisms.
- Acquire field imagery for crop, pest and soil analysis.
- Explore compact AI models suitable for resource-constrained edge computing.
- Build a modular software architecture for sensing, processing and presenting field observations.

## 4. System Architecture

| Subsystem | Main components / platform | Responsibility |
|---|---|---|
| Mobility | Chassis, DC drive motors, BTS7960 motor drivers | Rover movement and steering |
| Embedded control | Arduino UNO | Motor, servo, relay and ultrasonic control |
| Edge computing | Raspberry Pi 3B+ | Intended host for image processing, AI inference and application coordination |
| Distance sensing | HC-SR04-compatible ultrasonic interface in firmware | Distance measurement |
| Camera positioning | Pan servo | Camera/sensor orientation |
| Soil interaction | Drill actuator servos, NPK actuator servos, drill DC motor and relay | Mechanical soil-interaction operations |
| Application layer | Flask application directory | Web application / dashboard development |
| AI workstreams | Experimental computer-vision models | Pest, crop-disease, soil and leaf analysis |

### Conceptual data flow

```text
                    AGRICULTURAL FIELD
                            |
                            v
                 +----------------------+
                 |    M.O.O.N. ROVER    |
                 |   Mobile Platform    |
                 +----------------------+
                      |            |
              +-------+            +--------+
              |                             |
              v                             v
      +---------------+             +---------------+
      | Mobility and  |             | Field sensing |
      | soil actuators|             | and camera    |
      +---------------+             +---------------+
              |                             |
              +-------------+---------------+
                            |
                            v
                 +----------------------+
                 |     ARDUINO UNO      |
                 | Motion / Actuators   |
                 | Ultrasonic Interface |
                 +----------------------+
                            |
                   Serial / Integration
                            |
                            v
                 +----------------------+
                 |   RASPBERRY PI 3B+   |
                 | Edge-side Computing  |
                 +----------------------+
                            |
                            v
                 +----------------------+
                 |  COMPUTER VISION /   |
                 |       AI MODELS      |
                 +----------------------+
                            |
                            v
                 +----------------------+
                 | APPLICATION / DATA   |
                 | PRESENTATION LAYER   |
                 +----------------------+
```

*The diagram represents the intended high-level architecture. The exact communication protocol and complete integration between the Raspberry Pi, Arduino, sensors and application should be treated as under development unless demonstrated in the source code.*

## 5. Hardware Inventory

The following inventory is consolidated from the repository's Arduino controller firmware, project documentation and development log.

### 5.1 Main computing and control

| Component | Documented specification | Function |
|---|---|---|
| Raspberry Pi | Raspberry Pi 3B+ | Edge-computing platform for image handling, AI experiments and application integration |
| Microcontroller | Arduino UNO | Low-level rover movement and actuator control |
| Motor driver | BTS7960, left and right channels defined in firmware | High-current drive interface for the rover's motor groups |

### 5.2 Mobility and actuation

| Component | Documented specification | Function |
|---|---|---|
| Rover chassis | Approx. 2 ft × 2 ft | Mechanical platform |
| Drive system | Four-wheel arrangement | Field mobility |
| DC drive motors | Four-motor arrangement documented | Propulsion |
| Camera / sensor pan servo | Servo output on Arduino pin 4 | Camera or sensor positioning |
| Drill actuator servos | Two MG996R 360° continuous-rotation servo channels in firmware | Drill mechanism movement |
| NPK actuator servos | Two MG996R 360° continuous-rotation servo channels in firmware | NPK mechanism movement |
| Drill motor | DC motor switched through a relay output | Drill operation |
| Relay control | Arduino digital output pin 2 | Drill motor ON/OFF switching |

### 5.3 Sensing and imaging

| Component | Evidence in repository | Function / status |
|---|---|---|
| Ultrasonic distance sensor | Trigger and echo pins are defined in Arduino firmware | Distance measurement |
| Camera | Camera acquisition is part of the project architecture and workstream | Crop / soil image capture; integration status to be validated |
| DHT11 | Listed in the existing project hardware documentation | Temperature and relative-humidity sensing; firmware integration not established by the current controller sketch |
| MQ-135 | Listed in the existing project hardware documentation | Air-quality / gas-response sensing; firmware integration not established by the current controller sketch |

**Inventory accuracy note:** The firmware explicitly defines the BTS7960 motor-driver channels, pan servo, four actuator-servo channels, drill relay and ultrasonic sensor interface. The DHT11 and MQ-135 appear in the project's documented hardware list, but their pin assignments and operation are not present in the controller sketch reviewed for this README. Verify physical quantities, exact module variants, voltage/current ratings and wiring against the assembled rover before using this table as a procurement BOM.

## 6. Embedded Control and Firmware

The Arduino controller sketch is available at:

- [Arduino rover controller](moon_rover/arduino/moon_rover_controller.ino)
- [Additional locomotion demonstration sketch](Inventory/rover_locomotion_demo.ino)

The current controller firmware includes the following control groups:

| Function | Firmware interface |
|---|---|
| Forward / reverse | W / S |
| Stop rover | X |
| Spin left / right | A / D |
| Drill actuator down / up / stop | 1 / 2 / 3 |
| NPK actuator down / up / stop | 4 / 5 / 6 |
| Drill DC motor ON / OFF | O / F |
| Camera pan center / left / right | C / L / R |
| Read ultrasonic distance | U |
| Display command menu | M |

The sketch uses Arduino serial communication at **9600 baud** for its command interface. The left and right motor channels are controlled using PWM outputs and direction selection. The ultrasonic distance routine measures echo duration and converts it to an approximate distance in centimetres.

### Controller pin allocation

| Function | Arduino pin(s) |
|---|---|
| Ultrasonic trigger / echo | A0 / A1 |
| Camera pan servo | D4 |
| Left BTS7960 RPWM / LPWM | D3 / D5 |
| Left BTS7960 REN / LEN | D7 / D8 |
| Right BTS7960 RPWM / LPWM | D6 / D11 |
| Right BTS7960 REN / LEN | D10 / D12 |
| Drill actuator servos | A2 / A3 |
| NPK actuator servos | A4 / A5 |
| Drill motor relay | D2 |

*Pin allocation is reproduced from the current Arduino controller source. Confirm the physical wiring and driver-board terminal labels before powering the system.*

## 7. Software and AI Workstreams

| Area | Tools / platform | Purpose |
|---|---|---|
| Embedded programming | Arduino IDE, Arduino C/C++ | Motion and actuator control |
| Edge computing | Raspberry Pi OS, Python | On-device processing and application coordination |
| Computer vision | OpenCV | Image-processing workflows |
| Model experimentation | Google Colab | Model training and evaluation |
| Dataset sourcing | Kaggle datasets | Training and testing data |
| Web application | Flask | Application and dashboard development |
| 3D design resource | OBJ model | Mechanical / design reference |

### Agricultural AI modules under development

1. **Pest detection** — image-based identification of visible agricultural pests.
2. **Crop-disease recognition** — classification of crop or leaf images for potential disease symptoms.
3. **Soil classification** — image-based exploration of soil-category recognition.
4. **Leaf yellow-index analysis** — image segmentation and estimation of yellow and non-yellow leaf regions.

The work log records dataset collection and model training/testing using Kaggle datasets and Google Colab. Further validation is required for field accuracy, model robustness, inference speed and deployment performance on the Raspberry Pi 3B+.

## 8. Mechanical Design and Prototype Development

The rover's documented footprint is approximately **2 ft × 2 ft**. The development log records that Version 1 was tested and mechanical design anomalies were identified. The structure was subsequently reconsidered with the objective of improving stability.

The design includes a mobile chassis and dedicated mechanisms for drill and NPK-related soil interaction. The repository also contains a 3D OBJ model for design reference.

## 9. Project Media Gallery

All photographs and videos below are linked from the repository's `Inventory/` directory. The gallery is arranged by the available filename timestamps to provide a chronological development record. Captions identify the media sequence rather than asserting unverified component details.

### 9.1 Design and initial prototype resources

<p align="center">
  <img src="Inventory/Untitled%20Design.jpg" width="48%" alt="Rover design reference">
  <img src="Inventory/6.jpeg" width="48%" alt="Project design photograph">
</p>

<p align="center">
  <img src="Inventory/rover_version_1.jpg" width="48%" alt="Rover Version 1">
  <img src="Inventory/1b2e333b-b999-4ff9-99aa-126fafdfacf6.jpg" width="48%" alt="Rover project photograph">
</p>

### 9.2 Prototype and hardware documentation — 22 November 2026

<p align="center">
  <img src="Inventory/WhatsApp%20Image%202026-11-22%20at%208.57.33%20PM.jpeg" width="48%" alt="Prototype documentation, 8:57:33 PM">
  <img src="Inventory/WhatsApp%20Image%202026-11-22%20at%208.57.34%20PM.jpeg" width="48%" alt="Prototype documentation, 8:57:34 PM">
</p>

<p align="center">
  <img src="Inventory/WhatsApp%20Image%202026-11-22%20at%208.57.34%20PM%20(1).jpeg" width="48%" alt="Prototype documentation, 8:57:34 PM, additional view">
  <img src="Inventory/WhatsApp%20Image%202026-11-22%20at%208.57.35%20PM.jpeg" width="48%" alt="Prototype documentation, 8:57:35 PM">
</p>

<p align="center">
  <img src="Inventory/WhatsApp%20Image%202026-11-22%20at%208.57.35%207.jpeg" width="48%" alt="Prototype documentation, 8:57:35 PM, additional view">
  <img src="Inventory/WhatsApp%20Image%202026-11-22%20at%208.57.36%20PM.jpeg" width="48%" alt="Prototype documentation, 8:57:36 PM">
</p>

<p align="center">
  <img src="Inventory/WhatsApp%20Image%202026-11-22%20at%208.57.36%20PM%20(1).jpeg" width="48%" alt="Prototype documentation, 8:57:36 PM, additional view">
  <img src="Inventory/WhatsApp%20Image%202026-11-22%20at%208.57.36%20PM%20(2).jpeg" width="48%" alt="Prototype documentation, 8:57:36 PM, additional view">
</p>

<p align="center">
  <img src="Inventory/WhatsApp%20Image%202026-11-22%20at%208.57.36%20PM%20(3).jpeg" width="48%" alt="Prototype documentation, 8:57:36 PM, additional view">
  <img src="Inventory/WhatsApp%20Image%202026-11-22%20at%208.57.37%20PM.jpeg" width="48%" alt="Prototype documentation, 8:57:37 PM">
</p>

<p align="center">
  <img src="Inventory/WhatsApp%20Image%202026-11-22%20at%208.57.38%20PM.jpeg" width="48%" alt="Prototype documentation, 8:57:38 PM">
  <img src="Inventory/8b293d74-b255-4940-9a00-30b70bd94920.jpg" width="48%" alt="Rover project photograph">
</p>

### 9.3 Further development and testing records

<p align="center">
  <img src="Inventory/WhatsApp%20Image%202026-11-22%20at%209.05.04%20PM.jpeg" width="48%" alt="Development record, 9:05:04 PM">
  <img src="Inventory/WhatsApp%20Image%202026-11-22%20at%209.05.05%20PM.jpeg" width="48%" alt="Development record, 9:05:05 PM">
</p>

<p align="center">
  <img src="Inventory/WhatsApp%20Image%202026-11-22%20at%209.23.47%20PM.jpeg" width="48%" alt="Development record, 9:23:47 PM">
  <img src="Inventory/WhatsApp%20Image%202026-11-22%20at%209.25.14%20PM.jpeg" width="48%" alt="Development record, 9:25:14 PM">
</p>

<p align="center">
  <img src="Inventory/WhatsApp%20Image%202026-11-22%20at%209.26.21%20PM.jpeg" width="48%" alt="Development record, 9:26:21 PM">
  <img src="Inventory/WhatsApp%20Image%202026-11-22%20at%209.26.22%20PM.jpeg" width="48%" alt="Development record, 9:26:22 PM">
</p>

<p align="center">
  <img src="Inventory/WhatsApp%20Image%202026-11-22%20at%209.26.26%20PM.jpeg" width="48%" alt="Development record, 9:26:26 PM">
</p>

### 9.4 Demonstration videos

- [Prototype / rover demonstration — 8:57 PM](Inventory/WhatsApp%20Video%202026-11-22%20at%208.57.34%20PM.mp4)
- [Rover testing / development demonstration — 9:05 PM](Inventory/WhatsApp%20Video%202026-11-22%20at%209.05.04%20PM.mp4)

### 9.5 CAD, firmware and project documents

- [3D rover model — `tinker.obj`](Inventory/tinker.obj)
- [Locomotion demonstration firmware — `rover_locomotion_demo.ino`](Inventory/rover_locomotion_demo.ino)
- [Official SIH 2026 project document](Inventory/MOON_SIH2026_Official_Template_Fitted_Final90.pdf)
- [Inventory and work logs](Inventory/Inventory%20%26%20Work%20Logs)
- [Main Arduino controller firmware](moon_rover/arduino/moon_rover_controller.ino)

## 10. Repository Structure

```text
M.O.O.N-Field_Rover/
├── Inventory/
│   ├── Prototype photographs
│   ├── Prototype demonstration videos
│   ├── rover_locomotion_demo.ino
│   ├── tinker.obj
│   ├── Inventory & Work Logs
│   └── MOON_SIH2026_Official_Template_Fitted_Final90.pdf
├── docs & papers/
│   └── Agritech Rover Hardware Architecture (1).pdf
├── moon_rover/
│   ├── arduino/
│   │   └── moon_rover_controller.ino
│   └── my_flask_app/
│       └── templates/
└── README.md
```

## 11. Development Log

The repository's work log records the following contributions on **22 November 2026**.

| Contributor | Recorded work |
|---|---|
| Ishan Samanta — Project Lead | Rover redesign and restructuring; Raspberry Pi 3B+ setup; controller-board circuit connections; Arduino motion and servo-control programming; edge-computing model research; Version 1 testing and mechanical review |
| Shouvik Show — Project Member | Rover design and dimensional planning; AI model development for pest detection, crop-disease detection, yellow-index analysis and soil classification; Kaggle dataset collection; Google Colab training/testing; Version 1 testing and mechanical review |

## 12. Current Status and Roadmap

- [x] Initial four-wheel rover prototype documented.
- [x] Raspberry Pi 3B+ and Arduino UNO selected for the computing/control architecture.
- [x] Arduino controller firmware created for movement, actuator control, drill relay and ultrasonic distance reading.
- [x] 3D model and prototype media added to the repository.
- [x] Initial agricultural AI model experimentation recorded.
- [x] Version 1 tested and mechanical improvement areas identified.
- [ ] Complete and validate the revised mechanical structure.
- [ ] Verify motor-driver wiring, motor ratings and power distribution.
- [ ] Integrate and validate camera and field-sensor acquisition.
- [ ] Establish reliable Raspberry Pi–Arduino communication.
- [ ] Benchmark lightweight AI models on the Raspberry Pi 3B+.
- [ ] Integrate the AI workflow with the Flask application.
- [ ] Conduct repeatable field trials and publish measured results.

## 13. Engineering and Safety Considerations

| Area | Design consideration |
|---|---|
| Mechanical stability | Centre of gravity, chassis rigidity, wheel traction and actuator loads |
| Motor drive | Driver current rating, motor stall current, heat dissipation and wiring gauge |
| Power architecture | Suitable battery capacity, regulated logic supply, common reference where required and protection |
| Servo / actuator supply | Separate supply capability appropriate to servo current demand; avoid powering high-current servos from Arduino 5 V |
| Edge computing | Raspberry Pi memory, CPU load, model size and inference time |
| Sensor reliability | Calibration, placement and environmental interference |
| Field operation | Dust, moisture, vibration, cable retention and enclosure protection |

**Safety note:** The firmware controls motors, servos and a relay-driven drill motor. Test with wheels raised or the mechanism unloaded where practical, provide an accessible emergency power disconnect, and verify driver, relay, battery and actuator ratings before field operation.

## 14. Documentation and References

- [GitHub repository](https://github.com/ishansamanta/M.O.O.N-Field_Rover)
- [Project inventory](Inventory/)
- [Hardware architecture document](docs%20%26%20papers/Agritech%20Rover%20Hardware%20Architecture%20(1).pdf)
- [Official SIH 2026 project document](Inventory/MOON_SIH2026_Official_Template_Fitted_Final90.pdf)
- [Raspberry Pi documentation](https://www.raspberrypi.com/documentation/)
- [Arduino documentation](https://docs.arduino.cc/)
- [OpenCV documentation](https://docs.opencv.org/)
- [Flask documentation](https://flask.palletsprojects.com/)

## 15. Future Scope

Potential extensions include improved terrain handling, calibrated environmental and soil sensing, robust soil-sampling mechanisms, optimized edge-AI inference, offline field-data storage, dashboard-based historical analysis and extended agricultural field validation.

## 16. Project Status

M.O.O.N. is an active agricultural robotics development project. The repository contains prototype media, controller firmware, a 3D model, project documentation and AI experimentation records. System-level performance, sensing accuracy and field readiness will be established through further integration and testing.

---

<p align="center">
  <strong>M.O.O.N. — Intelligent Agricultural Field Rover</strong><br>
  <em>Connecting robotics, embedded systems and AI for precision agriculture.</em><br><br>
  <strong>SMART INDIA HACKATHON 2026</strong>
</p>
