# GestureCam AI

GestureCam AI is a gesture-controlled smart camera system built on a Raspberry Pi.
It uses computer vision to detect hand gestures and trigger camera actions in real time.

The system combines **OpenCV**, **MediaPipe**, and the **Raspberry Pi Camera** to create an interactive gesture-controlled interface.

---

# Features

* Real-time hand detection
* Finger counting
* Gesture recognition
* Gesture-controlled photo capture
* FPS counter display
* Simple UI overlay for gesture feedback

---

# Hardware Requirements

* Raspberry Pi 4 Model B
* Raspberry Pi Camera Module
* MicroSD Card (32GB recommended)
* Raspberry Pi OS

---

# Software Requirements

* Python 3
* OpenCV
* MediaPipe
* Picamera2
* NumPy

---

# Quick Setup (Recommended)

The easiest way to install and run the project is using the **setup script**.

Clone the repository:

```bash
git clone https://github.com/Om-18/GestureCam-AI.git
cd GestureCam-AI
```

Make the setup script executable:

```bash
chmod +x setup.sh
```

Run the setup script:

```bash
./setup.sh
```

After the setup finishes, activate the virtual environment:

```bash
source gc_venv/bin/activate
```

Run the program:

```bash
python gesturecam_ai.py
```

---

# Setup Script

The `setup.sh` script automatically performs the following tasks:

* Updates system packages
* Installs Raspberry Pi camera dependencies
* Creates a Python virtual environment
* Installs Python project dependencies
* Configures the environment for Picamera2

This ensures the project runs correctly on Raspberry Pi with minimal manual setup.

---

# Manual Installation

If you prefer to install everything manually, follow these steps.

Clone the repository:

```bash
git clone https://github.com/Om-18/GestureCam-AI.git
cd GestureCam-AI
```

Create a virtual environment:

```bash
python3 -m venv cam_env
source cam_env/bin/activate
```

Install Raspberry Pi camera libraries:

```bash
sudo apt install python3-picamera2 libcamera-apps
```

Install dependencies:

```bash
pip install -r requirements.txt
```
`
#  Allow venv to see system packages for camera
echo "/usr/lib/python3/dist-packages" > gc_venv/lib/python3.11/site-packages/system-packages.pth

---

# Running the Program

Activate the environment:

```bash
source gc_venv/bin/activate
```

Start the gesture detection system:

```bash
python gesturecam_ai.py
```

The camera will open and begin detecting hand gestures in real time.

---

# Gesture Controls

| Gesture        | Action           |
| -------------- | ---------------- |
| ✊ Fist         | Stop monitoring  |
| ☝️ One finger  | Start monitoring |
| ✌️ Two fingers | Capture photo    |
| 🖐 Open palm   | Exit program     |

---

# Project Structure

```
GestureCam-AI
│
├── gesturecam_ai.py
├── motion_detection.py
├── finger_counter.py
│
├── setup.sh
├── requirements.txt
├── README.md
│
├── docs
│   └── flowcharts.md
│
└── images
```

---

# How It Works

Camera Feed
↓
Hand Detection using MediaPipe
↓
21 Hand Landmarks Extraction
↓
Finger Position Analysis
↓
Gesture Recognition
↓
Trigger Camera Action

---

# Documentation

Detailed system diagrams and internal workflow charts can be found in:

```
docs/flowcharts.md
```

---

# Future Improvements

* Gesture-controlled IoT devices
* Hand sign language recognition
* Object detection integration
* Remote monitoring system
* Mobile or web dashboard

---

# Author

Om

---

