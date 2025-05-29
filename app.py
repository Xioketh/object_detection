from flask import Flask, render_template, request, jsonify
import subprocess
import sys
from pathlib import Path

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run-detection', methods=['POST'])
def run_detection():
    try:
        script_path = Path('yolov9/detect_dual.py').resolve()
        weights_path = Path(__file__).parent / 'yolov9' / 'yolov9-c.pt'
        vid_path = Path(__file__).parent / 'yolov9' / 'testwalk.mp4'

        command = [
            sys.executable,
            str(script_path),
            '--weights', str(weights_path),
            '--source', str(vid_path),
            '--device', 'cpu',
            '--view-img'
        ]

        # Run the command in the background
        subprocess.Popen(command)

        return jsonify({"status": "success", "message": "Detection started successfully"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)