from flask import Flask, request
import os
import cv2
import mediapipe as mp
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
        
if __name__ == '__main__':
    app.run()
