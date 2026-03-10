#!/bin/bash

# -----------------------------
# GestureCam-AI Setup Script
# -----------------------------

echo "Starting GestureCam-AI setup..."

# 1️⃣ Update system packages
sudo apt update
sudo apt upgrade -y

# 2️⃣ Install Raspberry Pi camera dependencies
echo "Installing Raspberry Pi camera libraries..."
sudo apt install -y python3-picamera2 libcamera-apps libatlas-base-dev libjpeg-dev

# 3️⃣ Create virtual environment
echo "Creating Python virtual environment..."
python3 -m venv gc_venv

# 4️⃣ Activate venv
source gc_venv/bin/activate

# 5️⃣ Upgrade pip
echo "Upgrading pip, setuptools, wheel..."
pip install --upgrade pip setuptools wheel

# 6️⃣ Install Python packages
echo "Installing Python dependencies..."
pip install -r requirements.txt

# 7️⃣ Allow venv to see system packages for camera
echo "/usr/lib/python3/dist-packages" > gc_venv/lib/python3.11/site-packages/system-packages.pth

echo "Setup complete!"
echo "Activate the virtual environment using:"
echo "source gc_venv/bin/activate"
echo "Then run:"
echo "python gesturecam_ai.py"
