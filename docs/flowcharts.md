# GestureCam AI – System Flowcharts

This document explains the internal workflow of the GestureCam AI system.

Built on Raspberry Pi using MediaPipe and OpenCV.

---

# 1. System Workflow

```mermaid
flowchart TD

A[Start Program] --> B[Initialize Camera]
B --> C[Capture Frame]

C --> D[Convert Frame to RGB]
D --> E[MediaPipe Hand Detection]

E --> F{Hand Detected?}

F -->|No| C
F -->|Yes| G[Extract 21 Hand Landmarks]

G --> H[Analyze Finger Positions]

H --> I[Recognize Gesture]

I --> J{Gesture Type}

J -->|FIST| K[Stop Monitoring]
J -->|ONE| L[Start Monitoring]
J -->|TWO| M[Capture Photo]
J -->|FIVE| N[Exit Program]

K --> C
L --> C
M --> C
N --> O[End Program]
```

---

# 2. Gesture Recognition Logic

```mermaid
flowchart TD

A[Landmarks Detected] --> B[Check Thumb Position]
B --> C[Check Index Finger]
C --> D[Check Middle Finger]
D --> E[Check Ring Finger]
E --> F[Check Pinky Finger]

F --> G[Count Raised Fingers]

G --> H{Finger Count}

H -->|0| I[FIST]
H -->|1| J[ONE]
H -->|2| K[TWO]
H -->|3| L[THREE]
H -->|4| M[FOUR]
H -->|5| N[FIVE]
```

---

# 3. High-Level System Architecture

```mermaid
flowchart LR

Camera --> RaspberryPi
RaspberryPi --> MediaPipe
MediaPipe --> GestureRecognition
GestureRecognition --> ActionController

ActionController --> PhotoCapture
ActionController --> MonitoringControl
ActionController --> ExitSystem
```
