# DriveSafe-AI 🚗

**Real-Time Driver Drowsiness Detection Using Computer Vision**

DriveSafe-AI is a prototype that uses a webcam to detect prolonged eye closure and can trigger an audible alert through an Arduino-connected buzzer.

> **Important:** This repository contains a webcam + MediaPipe EAR prototype. It does not currently implement EfficientNet-Lite2, a Temporal Convolutional Network (TCN), yawning detection, GPS, or Raspberry Pi deployment unless you add and test those components yourself.

## Features

- Real-time webcam capture with OpenCV
- Facial landmark detection using MediaPipe Face Mesh
- Eye Aspect Ratio (EAR) calculation
- Prolonged eye-closure detection
- On-screen EAR, status, and closure duration
- Optional Arduino serial communication and buzzer alert
- Webcam-only mode if the Arduino is unavailable

## Technology Stack

- Python 3.11 (recommended)
- OpenCV
- MediaPipe Face Mesh
- NumPy
- PySerial
- Arduino IDE / compatible Arduino board

## Repository Structure

```text
DriveSafe-AI/
├── webcam.py
├── arduino/
│   └── buzzer.ino
├── assets/
│   └── (add your screenshots and project photos here)
├── requirements.txt
├── TEAM.md
├── .gitignore
└── README.md
```

## Hardware Requirements

- Computer/laptop with a webcam
- Arduino-compatible board (optional for webcam-only testing)
- Active buzzer
- Jumper wires
- USB cable

### Example wiring

- Buzzer positive/red wire → Arduino digital pin 8
- Buzzer negative/black wire → Arduino GND

Check your buzzer's voltage/current requirements and your board's specifications before wiring. If you used a different pin or buzzer type, update the sketch accordingly. Disconnect power before changing wiring.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/DriveSafe-AI.git
cd DriveSafe-AI
```

Replace `YOUR-USERNAME` with the repository owner's GitHub username.

### 2. Create a Python virtual environment

On Windows with Python 3.11 installed:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

If `py -3.11` is not recognized, install Python 3.11 and ensure the Python Launcher is available.

### 3. Upload the Arduino sketch

1. Open `arduino/buzzer.ino` in the Arduino IDE.
2. Select the correct board and port.
3. Upload the sketch.
4. Close the Arduino Serial Monitor before starting Python.

The example sketch assumes an **active buzzer** connected to digital pin 8 and GND.

### 4. Set the serial port

Open `webcam.py` and change:

```python
SERIAL_PORT = "COM3"
```

to the Arduino's actual port (for example, `COM4`). Find it in Windows Device Manager under **Ports (COM & LPT)** or in the Arduino IDE.

If the Arduino is not connected, the Python program can still run in webcam-only mode.

### 5. Run the application

```powershell
.\.venv\Scripts\python.exe webcam.py
```

A window should display the webcam feed and detection status. Press **q** to quit.

## How It Works

1. OpenCV captures frames from the webcam.
2. MediaPipe Face Mesh estimates facial landmarks.
3. The program calculates EAR from six landmarks per eye.
4. When EAR stays below a configurable threshold for a set duration, the program labels the state as drowsy.
5. Python sends `1` to Arduino to activate the buzzer and `0` to stop it.

## Configuration

At the top of `webcam.py`:

```python
EAR_THRESHOLD = 0.20
DROWSY_TIME = 1.5
SERIAL_PORT = "COM3"
BAUD_RATE = 9600
```

These are starting values, not universally valid thresholds. Calibrate and test in the intended lighting and camera position. Eye closure is only a rough indicator and can produce false alarms or miss drowsiness.

## Team Members

See [`TEAM.md`](TEAM.md). Replace the placeholders with the actual names, GitHub usernames, and contributions of all team members.

## Screenshots and Demo

Add screenshots or a short demonstration to the `assets/` folder. Use only media that you have permission to share and avoid uploading identifiable recordings without consent.

Example Markdown after adding a screenshot:

```markdown
![DriveSafe-AI demo](assets/demo-screenshot.png)
```

## Limitations and Safety

- This is an educational prototype, not a certified or validated driver-monitoring device.
- Performance may vary with lighting, camera angle, glasses, occlusion, and individual facial characteristics.
- It uses prolonged eye closure and does not infer every cause of driver fatigue.
- Do not rely on this prototype as the sole safety measure while driving.

## Future Enhancements

Only mark these as completed after implementing and testing them:

- Yawning detection using mouth landmarks
- Temporal classification using a validated dataset
- Model evaluation and documented performance metrics
- Raspberry Pi deployment and low-light camera support
- GPS-based alerting

## License

Choose a license only after the team agrees on how the project may be reused. If you add a license, include the corresponding `LICENSE` file.
