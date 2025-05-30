# 🧠 YOLOv9 + Deep SORT Object Tracking System

This project implements **real-time object detection and tracking** using **YOLOv9** and **Deep SORT**. It detects and tracks multiple objects (like people, vehicles, etc.) across video frames, draws bounding boxes, assigns unique IDs, counts objects, and displays motion trails.

> 🔥 Includes demo footage generated via **Google Veo 2** to simulate a shopping mall-like scenario with vehicles and people in motion.

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
your-repo/
├── deep_sort_pytorch/         # Deep SORT tracking
├── runs/                      # Saved runs with output
├── data/                      # Input files (images/videos)
├── yolov9-c.pt                # YOLOv9 weights file
├── your_script.py             # Main entrypoint
├── requirements.txt
└── README.md
```

---

## 💾 Model Weights

Download `yolov9-c.pt` and place it in the root directory of your project.

**Path:**
```
./yolov9-c.pt
```

📥 Download: [YOLOv9 GitHub (WongKinYiu)](https://github.com/WongKinYiu/yolov9)

---

## 🔧 Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
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

### Run Tracking on a Video
```bash
python your_script.py --weights yolov9-c.pt --source data/demo_video.mp4 --view-img
```

- `--weights`: Path to YOLO model weights
- `--source`: Path to video/image/webcam/stream
- `--view-img`: Displays the result in a window

> Demo video generated with Google Veo 2: simulated urban/public environment with vehicles and people.

---

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

## 🎥 Demo Preview

> Video generated with **Google Veo 2** using the prompt:
>  
> `"Aerial view of a busy city street with people walking, cars driving, and traffic lights, high quality, cinematic look"`

✅ This makes the demo visually appealing for showcasing tracking in real-world scenarios.

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
- [Google Veo 2](https://ai.google/discover/veo/) for AI-generated demo video

---

## 📬 Contact

Connect with me on [LinkedIn](https://linkedin.com/in/your-profile) for collaboration, questions, or professional inquiries.

---