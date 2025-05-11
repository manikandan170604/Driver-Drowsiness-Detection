# Driver Drowsiness Detection

This project is aimed at detecting drowsiness in drivers using computer vision and machine learning techniques. By monitoring the driver's eye movements in real-time, the system can identify signs of fatigue and issue alerts to prevent road accidents.

## 🧠 Project Summary

The system captures video through a webcam, detects facial landmarks using `dlib`, calculates Eye Aspect Ratio (EAR) to monitor blinking and eye closure, and triggers an alarm using `pygame` if signs of drowsiness are detected. The project is developed with a Flask-based web interface.

## 📌 Features

- Real-time face and eye detection using OpenCV and dlib.
- EAR (Eye Aspect Ratio) based drowsiness detection algorithm.
- Alarm sound triggered when drowsiness is detected.
- Frontend with HTML, CSS, and JavaScript.
- Backend using Python (Flask framework).
- Uses pre-trained models and labeled datasets for training and testing.

## 🖥️ Technologies Used

**Frontend**:
- HTML
- CSS (CSS2, CSS3)
- JavaScript

**Backend**:
- Python
- Flask

**Libraries & Tools**:
- `OpenCV` (4.9.0)
- `dlib` (19.24.4)
- `pygame` (2.5.2)
- `scipy` (1.13.0)
- `imutils` (0.5.4)

## 💻 System Requirements

**Hardware**:
- Intel Core i3 7020U @2.30GHz
- 8GB RAM
- 1TB HDD
- Graphics card with 500MB

**Software**:
- Windows 10
- Visual Studio Code
- Python 3.x

## 🛠️ How It Works

1. Start video stream from the webcam.
2. Detect face and eyes using dlib’s 68-point landmark detector.
3. Calculate the Eye Aspect Ratio (EAR).
4. If EAR < threshold for a number of consecutive frames → trigger alarm.
5. Display the video and EAR data via a Flask-powered web interface.

## 🧾 Algorithm

**Eye Aspect Ratio (EAR)** is calculated as:

```
EAR = (||P2 - P6|| + ||P3 - P5||) / (2 * ||P1 - P4||)
```

If the EAR value stays below a threshold for a certain period, it indicates drowsiness.

## 📸 Screenshots

- Home page interface
- Real-time detection
- Alert system page
- Application closing screen

## 📁 Dataset

The dataset used includes both drowsy and non-drowsy labeled images and was sourced from:

- [Kaggle Dataset - Driver Drowsiness Detection](https://www.kaggle.com/datasets/talhabhatti7262/drivers-drowsiness-detection)

## 📋 Modules

- Face Detection
- Facial Landmark Detection
- EAR Calculation and Classification
- Drowsiness Alert System
- Web UI with Flask
- Integration with external vehicle systems

## 🔍 Testing

Includes:
- Unit Testing
- Integration Testing
- White Box Testing
- System Testing for performance and alert accuracy

## 🧰 Maintenance

The project follows corrective, adaptive, perfective, preventive, and evaluative maintenance practices to ensure functionality, scalability, and relevance.

## 👨‍💻 Contributor

- **K. Manikandan** - [21UL81]

Final Year BCA Students  
Ayya Nadar Janaki Ammal College (Autonomous), Sivakasi

## 📚 References

- [Python](https://www.learnpython.org)
- [Flask](https://flask.palletsprojects.com)
- [OpenCV](https://opencv.org)
- [dlib](http://dlib.net)
- [Kaggle](https://www.kaggle.com/datasets/talhabhatti7262/drivers-drowsiness-detection)

---

> **Note:** This system is a prototype and should be integrated into real-world vehicle systems with caution and further testing for reliability and safety.
