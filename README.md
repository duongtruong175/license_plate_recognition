# License Plate Reconigtion

### Nhận dạng biển số xe
Các bước biến hành:
1. Phát hiện vùng chứa biển số xe (dùng phương pháp Đường viền và YOLO)
2. Phân đoạn ký tự trong biển số xe
3. Nhận dạng các ký tự trong biển số xe

### Demo web
Code backend: https://github.com/hungvt639/-cv-lpr-backend

Code frontend: https://github.com/hungvt639/cv-lpr-frontend

Link web demo: http://lpr-cv.hung-vt.bike/

### Yêu cầu
Tải các file chứa dataset gồm: character_dataset, test_dataset, yolo_utils tại [đường dẫn](https://drive.google.com/drive/folders/1KUmpmUokHaG_j_ys3_KdrhZZ4F-36aoh?usp=sharing)

### Môi trường sử dụng
python 3.6.8

requirements.txt

### Cách chạy
- Tạo môi trưởng python 3.6.8

VD: cách tạo trên windows

b1: cần cài virtualenv và thêm path đầy đủ

b2: gọi lệnh tạo 1 môi trường ảo: virtualenv -p C:\Python36\python.exe btl

b3: đứng trong thư mục btl: chạy .\Scripts\activate

- Sau đó cd vào thư mục license_plate_recognition
- Cài thư viện: pip install -r requirements.txt
- Chạy các file .inpynb để test hệ thống
