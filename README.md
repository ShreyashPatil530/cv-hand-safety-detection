# 🖐️ CV Hand Safety Detection

> **A real-time computer vision prototype that detects hand proximity to dangerous zones using classical OpenCV techniques.**

[![Python 3.7+](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-green)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Maintained](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/ShreyashPatil530/cv-hand-safety-detection)

---

## 🎯 Overview

**cv-hand-safety-detection** is a lightweight, CPU-only computer vision proof-of-concept that performs real-time hand tracking and proximity detection. It uses classical OpenCV techniques (color segmentation, contour detection, and distance calculations) to classify hand positions as **SAFE**, **WARNING**, or **DANGER**.

### ✨ Key Highlights

- ✅ **No AI Models** — 100% classical computer vision (no MediaPipe, OpenPose, or cloud APIs)
- ✅ **CPU-Only** — Runs smoothly on any laptop at 8–20 FPS
- ✅ **Real-Time Tracking** — Live hand detection via webcam
- ✅ **Virtual Boundary Detection** — Customizable safety zones
- ✅ **Multi-State Alerts** — SAFE (green), WARNING (yellow), DANGER (red)
- ✅ **Easy to Extend** — Perfect foundation for gesture-based interactions

---

## 📋 Features

| Feature | Description |
|---------|-------------|
| 🖐️ **Hand Tracking** | HSV color segmentation + contour analysis |
| 📍 **Distance Calculation** | Real-time hand-to-boundary distance |
| 🎨 **Visual Feedback** | Color-coded state indicators + on-screen text |
| ⚙️ **Customizable Thresholds** | Adjust SAFE, WARNING, DANGER distances |
| 🚨 **Alert System** | Bold red "DANGER DANGER" overlay on critical proximity |
| 📊 **Performance Metrics** | FPS counter included |
| 🎯 **Lightweight** | Minimal dependencies, optimized for CPU |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Webcam or camera device
- 100 MB free disk space

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ShreyashPatil530/cv-hand-safety-detection.git
   cd cv-hand-safety-detection
   ```

2. **Create and activate virtual environment**
   
   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

Press **ESC** to exit the application.

---

## 📁 Project Structure

```
cv-hand-safety-detection/
├── main.py                 # Main application entry point
├── requirements.txt        # Project dependencies
├── LICENSE                 # MIT License
├── README.md              # This file
└── utils/
    ├── __init__.py
    └── hand_detection.py  # Core hand detection logic
```

---

## 🧠 How It Works

### 1. **Hand Detection Pipeline**

```
Video Frame
    ↓
Convert to HSV Color Space
    ↓
Apply Skin Color Mask
    ↓
Find Contours
    ↓
Extract Largest Contour (Hand)
    ↓
Calculate Center Point
    ↓
Draw on Frame
```

### 2. **Virtual Boundary System**

A customizable rectangular boundary is defined:
- **Top-Left Corner:** `(BOUNDARY_X1, BOUNDARY_Y1)`
- **Bottom-Right Corner:** `(BOUNDARY_X2, BOUNDARY_Y2)`

### 3. **Distance-Based State Classification**

```
Distance = ||Hand Center - Boundary Center||

SAFE:     distance > SAFE_DIST
WARNING:  WARNING_DIST < distance ≤ SAFE_DIST
DANGER:   distance < DANGER_DIST OR hand inside boundary
```

### 4. **Real-Time Visual Feedback**

| State | Color | Icon | Action |
|-------|-------|------|--------|
| **SAFE** | 🟢 Green | ✓ | Safe distance maintained |
| **WARNING** | 🟡 Yellow | ⚠️ | Hand approaching boundary |
| **DANGER** | 🔴 Red | ❌ | Hand too close / inside boundary |

---

## ⚙️ Configuration

Edit these parameters in `main.py` to customize behavior:

```python
# Boundary coordinates (adjust to your use case)
BOUNDARY_X1, BOUNDARY_Y1 = 200, 150
BOUNDARY_X2, BOUNDARY_Y2 = 600, 450

# Distance thresholds (in pixels)
SAFE_DIST = 150
WARNING_DIST = 80
DANGER_DIST = 30

# HSV color range for skin detection
LOWER_SKIN = np.array([0, 20, 70])
UPPER_SKIN = np.array([20, 255, 255])
```

---

## 🎬 Usage Example

```python
import cv2
from utils.hand_detection import HandDetector

# Initialize detector
detector = HandDetector()

# Capture video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    # Detect hand and get state
    frame, state = detector.process_frame(frame)
    
    # Display results
    cv2.imshow("Hand Safety Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
```

---

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| **FPS (CPU)** | 8–20 FPS |
| **Latency** | ~50–125 ms |
| **Memory Usage** | ~80–150 MB |
| **GPU Required** | No |
| **Python Version** | 3.7+ |

*Performance varies based on system specs and camera resolution.*

---

## 🔧 Technologies Used

- **Python 3.7+** — Core language
- **OpenCV 4.5+** — Classical computer vision library
- **NumPy** — Numerical computations

---

## 🚦 State Machine Diagram

```
        ┌─────────────────────────────────────┐
        │                                     │
        ▼                                     │
    ┌────────┐                               │
    │  SAFE  │ ◄─── Hand moves away          │
    └────────┘                               │
        │                                     │
        │ Hand approaches                     │
        ▼                                     │
    ┌─────────────┐                          │
    │   WARNING   │ ◄─── Hand moves away     │
    └─────────────┘                          │
        │                                     │
        │ Hand gets too close                │
        ▼                                     │
    ┌────────┐                               │
    │ DANGER │ ───────────────────────────────┘
    └────────┘
```

---

## 🔮 Future Improvements

- [ ] Multiple boundary zones
- [ ] Sound alerts on state change
- [ ] Motion tracking (optical flow analysis)
- [ ] Gesture recognition for commands
- [ ] Depth estimation for 3D proximity
- [ ] Machine learning calibration
- [ ] Web interface for live monitoring
- [ ] Video recording with state annotations

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Shreyash Patil**

- 🎓 Computer Vision & ML/AI Enthusiast
- 💼 Full-Stack Developer
- 🔗 GitHub: [@ShreyashPatil530](https://github.com/ShreyashPatil530)

---

## ⭐ Show Your Support

If this project helped you, please consider giving it a star! Your support motivates continued development.

```bash
git star https://github.com/ShreyashPatil530/cv-hand-safety-detection
```

---

## 📧 Contact & Support

- **Issues:** [GitHub Issues](https://github.com/ShreyashPatil530/cv-hand-safety-detection/issues)
- **Discussions:** [GitHub Discussions](https://github.com/ShreyashPatil530/cv-hand-safety-detection/discussions)

---

## 🙏 Acknowledgments

- OpenCV community for excellent documentation
- All contributors and testers

---

**Made with ❤️ by Shreyash Patil**
