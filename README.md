# 🚗 DriveSafe-AI
### Real-Time Driver Drowsiness Detection Using Computer Vision

## 📌 About the Project

DriveSafe-AI is a driver drowsiness detection system developed to identify signs of drowsiness by monitoring the driver's eyes through a webcam. When the system detects prolonged eye closure, it displays a warning on the screen and activates a buzzer connected to an Arduino.

The main aim of this project is to demonstrate how computer vision and hardware integration can be used to improve driver awareness and help reduce accidents caused by drowsiness.

## ✨ Features

- **Real-Time Eye Monitoring:** Captures live video using a webcam.
- **Facial Landmark Detection:** Uses MediaPipe Face Mesh to identify facial landmarks around the eyes.
- **Eye Aspect Ratio (EAR):** Calculates the EAR to estimate eye closure.
- **Drowsiness Detection:** Identifies prolonged eye closure based on a configurable threshold and duration.
- **Visual Alerts:** Displays the eye aspect ratio and the driver's current status on the screen.
- **Audible Alerts:** Activates an Arduino-connected buzzer when drowsiness is detected.
- **Flexible Operation:** Supports webcam-only testing when the Arduino is unavailable.

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe Face Mesh
- NumPy
- PySerial
- Arduino IDE
- Arduino-compatible board and buzzer

## 🔧 Hardware Requirements

- Laptop or computer with a webcam
- Arduino-compatible board
- Active buzzer
- Jumper wires
- USB cable

## ⚙️ How It Works

1. The webcam captures live video of the driver.
2. OpenCV processes the video frames.
3. MediaPipe Face Mesh detects facial landmarks around the eyes.
4. The Eye Aspect Ratio (EAR) is calculated using the detected landmarks.
5. If the EAR remains below the configured threshold for a specified duration, the system identifies a possible drowsiness condition.
6. A warning is displayed on the screen.
7. If the Arduino is connected, Python sends a serial command to activate the buzzer.

## 📂 Project Structure

```text
DriveSafe-AI/
├── webcam.py
├── arduino/
│   └── buzzer.ino
├── assets/
│   └── README.md
├── requirements.txt
├── TEAM.md
├── .gitignore
└── README.md
```

## 💻 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/keets970/DriveSafe-AI.git
cd DriveSafe-AI
```

### 2. Install Python Dependencies

Python 3.11 is recommended for this project.

Create a virtual environment on Windows:

```powershell
py -3.11 -m venv .venv
```

Install the required libraries:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 3. Configure the Arduino

1. Open `arduino/buzzer.ino` using the Arduino IDE.
2. Select the appropriate board and COM port.
3. Upload the program to the Arduino.
4. Connect the active buzzer to digital pin 8 and GND, following the hardware specifications.

### 4. Configure the Serial Port

Open `webcam.py` and check the serial port setting:

```python
SERIAL_PORT = "COM3"
```

Change `COM3` to the port assigned to your Arduino if necessary.

### 5. Run the Application

```powershell
.\.venv\Scripts\python.exe webcam.py
```

The webcam window displays the detection status. Press **q** to close the application.

## 🔍 Applications

- Driver awareness and drowsiness monitoring prototypes
- Computer vision learning and experimentation
- Real-time facial landmark analysis
- Python and Arduino hardware integration
- Educational projects related to road safety

## 🚀 Future Enhancements

- Yawning detection using facial landmarks
- Improved drowsiness classification using temporal models
- Testing with labelled datasets and performance evaluation
- Raspberry Pi deployment
- Low-light camera support
- GPS-based alerting

## ⚠️ Limitations

This project is an educational prototype that uses prolonged eye closure as an indicator of possible drowsiness. Its performance may vary depending on lighting, camera angle, glasses, and other conditions. It is not a certified driver-safety system and should not be used as the sole means of preventing accidents.

## 🎯 Conclusion

DriveSafe-AI demonstrates the practical application of computer vision for detecting prolonged eye closure and generating alerts. By combining Python, MediaPipe, OpenCV, and Arduino, the project provides hands-on experience in real-time image processing and hardware integration while exploring a technology relevant to road safety.
