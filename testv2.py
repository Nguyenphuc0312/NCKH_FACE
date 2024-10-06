import cv2
import py360convert

# Địa chỉ URL của camera IP
camera_url = "rtsp://admin:Dung@2811@192.168.0.202:554/stream1"

# Mở kết nối tới camera IP
# cap = cv2.VideoCapture(camera_url)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Không thể kết nối tới camera")
    exit()

# Tạo một cửa sổ với tùy chọn flag là WINDOW_NORMAL
cv2.namedWindow('Camera IP', cv2.WINDOW_NORMAL)

# Vòng lặp để hiển thị khung hình từ camera
while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Không thể nhận khung hình (kết nối có thể đã mất)")
        break
    
    # Kích thước đầu ra cho panorama
    out_hw = (frame.shape[1], frame.shape[0])  # Chiều rộng và chiều cao của hình ảnh gốc
    
    # Chuyển đổi khung hình từ equirectangular sang panorama
    panorama = py360convert.e2p(frame, fov_deg=[100, 100], v_deg=0, u_deg=0, out_hw=out_hw)

    window_width, window_height = cv2.getWindowImageRect('Camera IP')[2:4]
    
    # Tùy chỉnh kích thước khung hình về kích thước của cửa sổ
    resized_frame = cv2.resize(panorama, (window_width, window_height), interpolation=cv2.INTER_LINEAR)
    
    # Hiển thị khung hình đã thay đổi kích thước
    cv2.imshow('Camera IP', resized_frame)
    
    # Thoát khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
