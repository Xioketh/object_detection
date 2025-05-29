from flask import Flask
from threading import Lock
import cv2

class FlaskBridge:
    def __init__(self):
        self.frame = None
        self.frame_lock = Lock()
        self.object_counts = {}
        self.detection_active = True

flask_bridge = FlaskBridge()

def get_frame():
    with flask_bridge.frame_lock:
        if flask_bridge.frame is not None:
            ret, buffer = cv2.imencode('.jpg', flask_bridge.frame)
            return buffer.tobytes()
    return None

def get_counts():
    return flask_bridge.object_counts

def set_frame(frame):
    with flask_bridge.frame_lock:
        flask_bridge.frame = frame

def set_counts(counts):
    flask_bridge.object_counts = counts

def is_detection_active():
    return flask_bridge.detection_active

def set_detection_active(active):
    flask_bridge.detection_active = active