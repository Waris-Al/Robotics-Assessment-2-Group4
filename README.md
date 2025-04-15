# Intruder Detection System — VEX EXP + Raspberry Pi

This repository contains Vex and Raspberry Pi code for the security droid that Group 4 is creating for the second robotics assignment.
A video demonstration of the robot is also included and can be found at the link below.

https://youtu.be/zh6aF2zvjy0

---

## Hardware Components

- **VEX EXP Brain**
- **VEX Distance Sensor** (Port 1)
- **VEX Inertial Sensor**
- **VEX Motor** (Port 6, reversed)
- **Digital Out Signal** (3-wire port A)
- **Raspberry Pi** (with camera support)
- **PiCamera or USB Webcam**
- **Internet Connection** (for email functionality)

---

## System Overview

### VEX EXP Robot
- Rotates 180° in increments to scan for objects.
- Uses a Distance Sensor to detect objects within 45 inches.
- When an intruder is detected:
  - Displays "Intruder Detected" on the screen.
  - Sends a HIGH signal via a digital output to the Raspberry Pi.
  - Waits 5 seconds while video is recorded.
  - Resets the signal and continues scanning.

### Raspberry Pi
- Listens for HIGH signal from the VEX robot.
- When triggered:
  - Records a 10-second video.
  - Sends an email with the video as an attachment.
- Waits before listening again.

---

## Email Preview

**Subject:** INTRUDER ALERT!!  
**Body:** Please see the intruder in the attached video.  
**Attachment:** `Intruder_Alert.mp4`

> Use an **App Password** for Gmail. Do **not** use your real password in the script.

---

## Setup Instructions

### Raspberry Pi
1. Enable the camera module (using `raspi-config`).
2. Install required packages:
   ```bash
   pip install picamera RPi.GPIO
   ```
3. Edit `capture_intruder.py` with your email credentials and run the script.
