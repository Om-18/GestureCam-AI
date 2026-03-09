# GestureCam AI

GestureCam AI is a gesture-controlled smart camera system built on Raspberry Pi.  
It uses computer vision to detect hand gestures and trigger camera actions.

## Features

- Real-time hand detection
- Finger counting
- Gesture recognition
- Gesture-controlled photo capture
- FPS counter display
- Simple UI overlay

## Hardware Requirements

- Raspberry Pi 4 Model B
- Raspberry Pi Camera Module
- MicroSD card
- Raspberry Pi OS

## Software Requirements

- Python 3
- OpenCV
- MediaPipe
- Picamera2
- NumPy

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/GestureCam-AI.git
cd GestureCam-AI
```

Create virtual environment:

```bash
python3 -m venv cam_env
source cam_env/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Make sure Raspberry Pi camera libraries are installed:

```bash
sudo apt install python3-picamera2 libcamera-apps
```

## Running the Program

Activate the environment:

```bash
source cam_env/bin/activate
```

Run the gesture camera:

```bash
python gesturecam_ai.py
```

## Gesture Controls

| Gesture | Action |
|-------|------|
| ✊ Fist | Stop monitoring |
| ☝️ One finger | Start monitoring |
| ✌️ Two fingers | Capture photo |
| 🖐 Open palm | Exit program |

## Project Structure

```
GestureCam-AI
│
├── gesturecam_ai.py
├── motion_detection.py
├── finger_counter.py
├── requirements.txt
├── README.md
└── images/
```

## How it Works

Camera → Hand Detection (MediaPipe)  
→ 21 Hand Landmarks  
→ Finger State Detection  
→ Gesture Recognition  
→ Trigger Action

## Future Improvements

- Gesture controlled IoT devices
- Hand sign recognition
- Object detection integration
- Remote monitoring

## Author

Om
