# 🧠 YOLOv9 + Deep SORT Object Tracking System

This project implements **real-time object detection and tracking** using **YOLOv9** and **Deep SORT**. It detects and tracks multiple objects (like people, vehicles, etc.) across video frames, draws bounding boxes, assigns unique IDs, counts objects, and displays motion trails.

---

## 🚀 Features

- Multi-object tracking with persistent IDs  
- Real-time bounding box and label drawing  
- Unique object counter and display  
- Visualization of motion trails  
- JSON output with summary statistics  
- Option to use any video/image/webcam source  

---

## 📁 Folder Structure

```
Obj-Det/
├── templates/ 
├── yolov9/
       ├── deep_sort_pytorch/         # Deep SORT tracking
       ├── runs/                      # Saved runs with output
       ├── data/                      # Input files (images/videos)
       ├── yolov9-c.pt                # YOLOv9 weights file
       ├── detect_dual.py             # Main entrypoint
       ├── requirements.txt
├── app.py
└── README.md
```

---

## 💾 Model Weights

Download `yolov9-c.pt` and place it in the root directory of your project.

**Path:**
```
./yolov9-c.pt
```

📥 Download: [YOLOv9 GitHub (WongKinYiu)](https://github.com/WongKinYiu/yolov9/releases/tag/v0.1)

---

## 🔧 Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/Xioketh/object_detection.git
cd object_detection
```

### 2. (Optional) Create a Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies
```bash
cd yolov9
pip install -r requirements.txt
```

Make sure you have:
- Python 3.8+
- Torch >= 1.7
- OpenCV
- NumPy
- Matplotlib
- PyYAML
- and other YOLO/Deep SORT requirements

---

## 🛠️ Usage

### Run Project
```bash
python app.py
```


## 📊 Output

- Live window with tracked objects, IDs, and trails
- JSON file with unique object counts (`detection_results.json`)
- Annotated output video saved in:
  ```
  runs/detect/exp*/output.mp4
  ```

---

## 🧠 Classes Tracked

Tracking is done using COCO classes such as:

- `person`
- `car`
- `bus`
- `truck`
- `bicycle`
- `motorcycle`
- `dog`, `cat`, etc.

You can customize tracked classes in the code.

---

## 🌐 Optional Enhancements

- Add UI for selecting inputs
- Track only specific classes
- Save frame-wise metadata for analytics
- Use different YOLOv9 variants (e.g., `yolov9-e.pt`, `yolov9-d.pt`)

---

## 🧾 License

MIT License – feel free to use, modify, and distribute with proper credit.

---

## 🙌 Credits

- [YOLOv9 by WongKinYiu](https://github.com/WongKinYiu/yolov9)
- [Deep SORT by nwojke](https://github.com/nwojke/deep_sort)
---

## 📬 Contact

Connect with me on [LinkedIn](https://www.linkedin.com/in/kethaka-janadithya-ranasinghe-a73ab7242/) for collaboration, questions, or professional inquiries.

---