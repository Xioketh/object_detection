from flask import Flask, render_template, request, jsonify
import subprocess
import sys
import os
from werkzeug.utils import secure_filename
from pathlib import Path
import json

import torch
print(torch.cuda.is_available())  # Should print True
print(torch.cuda.get_device_name(0))


app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv'}


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run-detection', methods=['POST'])
def run_detection():
    try:
        # Check if the post request has the file part
        if 'video' not in request.files:
            return jsonify({"status": "error", "message": "No video file provided"}), 400

        file = request.files['video']

        # If user does not select file, browser might submit an empty part without filename
        if file.filename == '':
            return jsonify({"status": "error", "message": "No selected file"}), 400

        if file and allowed_file(file.filename):
            # Secure the filename and save it
            filename = secure_filename(file.filename)
            video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(video_path)

            print(f"Saved uploaded video to: {video_path}")
            print("Triggering YOLOv9 detection")
            print("Subprocess will use Python:", sys.executable)

            script_path = Path('yolov9/detect_dual.py').resolve()
            weights_path = Path(__file__).parent / 'yolov9' / 'yolov9-c.pt'

            command = [
                sys.executable,
                str(script_path),
                '--weights', str(weights_path),
                '--source', video_path,
                '--device', '0',
                '--view-img'
            ]

            # Run the command in the background
            subprocess.run(command, check=True)
            # subprocess.run(["ls", "-l"], check=True)
            # subprocess.run([command], check=True)

            save_dir_base = Path("yolov9/runs/detect")
            latest_dir = sorted(save_dir_base.glob("exp*"), key=os.path.getmtime)[-1]
            results_path = latest_dir / "detection_results.json"

            print("results_path::::::: ",results_path)

            if results_path.exists():
                with open(results_path, 'r') as f:
                    summary = json.load(f)
            else:
                summary = {"message": "Detection results not found"}

            return jsonify({
                "status": "success",
                "message": "Detection completed successfully",
                "filename": filename,
                "summary": summary
            })

        return jsonify({"status": "error", "message": "File type not allowed"}), 400

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)