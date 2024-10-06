import cv2
# from flask import Flask, render_template, Response





# Địa chỉ URL của camera IP
camera_url = "rtsp://admin:Dung@2811@192.168.0.202:554/stream1"

# Mở kết nối tới camera IP
# cap = cv2.VideoCapture(camera_url)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Không thể kết nối tới camera")
    exit()

#Tạo một cửa số với tuỳ chọn flag là WINDOW_NORMAL, tuỳ chọn này cho phép thay đổi kích thước cửa sổ
cv2.namedWindow('Camera IP', cv2.WINDOW_NORMAL)

# Vòng lặp để hiển thị khung hình từ camera
while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Không thể nhận khung hình (kết nối có thể đã mất)")
        break
    
    
    
    window_width, window_height = cv2.getWindowImageRect('Camera IP')[2:4]
    
    # Tùy chỉnh kích thước khung hình về 640x480 pixel
    resized_frame = cv2.resize(frame, (window_width, window_height), interpolation=cv2.INTER_LINEAR)
    # resized_frame = cv2.resize(frame, (640, 480), cv2.INTER_CUBIC)#cv2.INTER_CUBIC
    
    # Hiển thị khung hình đã thay đổi kích thước
    cv2.imshow('Camera IP', resized_frame)
    
    # Thoát khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()



# app = Flask(__name__)

# def gen_frames():
#     camera = cv2.VideoCapture(0)
#     while True:
#         success, frame = cap.read()
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/video_feed')
# def video_feed():
#     return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run(debug=True)