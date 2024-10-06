from flask import Flask, render_template, Response
import cv2
import os

app = Flask(__name__)

camera_url = "rtsp://admin:Dung@2811@192.168.0.202:554/stream1"

def gen_frames():
    cap = cv2.VideoCapture(0)  # Sử dụng camera máy tính
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = cv2.flip(frame, 1)
            frame = buffer.tobytes()
            
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
