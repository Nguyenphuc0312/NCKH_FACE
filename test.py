import cv2

# Địa chỉ URL của camera IP
camera_url = "rtsp://admin:Dung@2811@192.168.0.202:554/stream1"

# Mở kết nối tới camera IP
cap = cv2.VideoCapture(camera_url)

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


# import cv2
# import numpy as np

# # Địa chỉ URL của camera IP hoặc thay thế bằng webcam mặc định
# camera_url = "rtsp://admin:Dung@2811@192.168.0.202:554/stream1"
# # Hoặc sử dụng webcam mặc định
# # camera_url = 0

# # Mở kết nối tới camera IP hoặc webcam
# cap = cv2.VideoCapture(camera_url)

# if not cap.isOpened():
#     print("Không thể kết nối tới camera")
#     exit()

# # Kích thước đầu ra
# output_width = 800
# output_height = 600

# # Hàm để tạo ma trận chiếu
# def create_perspective_transform(fov, output_width, output_height):
#     # Góc nhìn (FOV - Field of View) trên cả hai trục
#     fov_rad = np.radians(fov / 2.0)

#     # Tính toán khoảng cách tiêu cự dựa trên FOV và kích thước đầu ra
#     focal_length = output_width / (2 * np.tan(fov_rad))

#     # Tạo ma trận chiếu từ tọa độ 3D về tọa độ 2D
#     perspective_matrix = np.array([
#         [focal_length, 0, output_width / 2],
#         [0, focal_length, output_height / 2],
#         [0, 0, 1]
#     ])

#     return perspective_matrix

# # Vòng lặp để hiển thị khung hình từ camera
# while True:
#     ret, frame = cap.read()

#     if not ret:
#         print("Không thể nhận khung hình (kết nối có thể đã mất)")
#         break

#     # Lấy kích thước ảnh gốc
#     h, w = frame.shape[:2]

#     # Tạo ma trận chiếu với FOV là 90 độ
#     perspective_matrix = create_perspective_transform(90, output_width, output_height)

#     # Lấy khung hình từ hình ảnh 360 với chiếu phẳng
#     output_frame = cv2.warpPerspective(frame, perspective_matrix, (output_width, output_height))

#     # Hiển thị hình ảnh đã được chiếu phẳng
#     cv2.imshow('Flat Projection', output_frame)

#     # Thoát khi nhấn phím 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# import cv2
# import numpy as np

# # Địa chỉ URL của camera IP hoặc webcam
# camera_url = "rtsp://admin:Dung@2811@192.168.0.202:554/stream1"
# # Hoặc sử dụng webcam mặc định
# # camera_url = 0

# # Mở kết nối tới camera IP hoặc webcam
# cap = cv2.VideoCapture(camera_url)

# if not cap.isOpened():
#     print("Không thể kết nối tới camera")
#     exit()

# # Kích thước đầu ra
# output_width = 800
# output_height = 600

# # Hàm để xử lý chiếu hình cầu
# def spherical_projection(frame):
#     # Lấy kích thước của khung hình
#     h, w = frame.shape[:2]

#     # Tạo lưới cho tọa độ x và y
#     y_indices, x_indices = np.indices((output_height, output_width))
    
#     # Chuyển đổi tọa độ pixel từ mặt phẳng sang tọa độ hình cầu
#     theta = (x_indices / output_width) * 2 * np.pi  # Góc ngang
#     phi = (y_indices / output_height) * np.pi       # Góc dọc

#     # Tính toán tọa độ x, y trong không gian 3D
#     x = np.sin(phi) * np.sin(theta)
#     y = np.cos(phi)
#     z = np.sin(phi) * np.cos(theta)

#     # Chuyển đổi tọa độ 3D về tọa độ 2D trong khung hình 360
#     x_equirectangular = (np.arctan2(x, z) + np.pi) / (2 * np.pi) * w
#     y_equirectangular = (np.arcsin(y) + np.pi / 2) / np.pi * h

#     # Lấy giá trị pixel từ khung hình 360
#     output_frame = np.zeros((output_height, output_width, 3), dtype=np.uint8)
#     for i in range(output_height):
#         for j in range(output_width):
#             x_equi = int(x_equirectangular[i, j])
#             y_equi = int(y_equirectangular[i, j])
#             if 0 <= x_equi < w and 0 <= y_equi < h:
#                 output_frame[i, j] = frame[y_equi, x_equi]

#     return output_frame

# # Vòng lặp để hiển thị khung hình từ camera
# while True:
#     ret, frame = cap.read()
    
#     if not ret:
#         print("Không thể nhận khung hình (kết nối có thể đã mất)")
#         break

#     # Xử lý chiếu hình cầu
#     output_frame = spherical_projection(frame)

#     # Hiển thị hình ảnh đã xử lý
#     cv2.imshow('Spherical Projection', output_frame)

#     # Thoát khi nhấn phím 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

