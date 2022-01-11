# License Plate Reconigtion
Nhận dạng biển số xe

Các bước biến hành:
1. Phát hiện vùng chứa biển số xe (dùng phương pháp Đường viền và YOLO)
2. Phân đoạn ký tự trong biển số xe
3. Nhận dạng các ký tự trong biển số xe

### Môi trường sử dụng
python 3.6.8

requirements.txt

### Cách chạy
- Tạo môi trưởng python 3.6.8

VD: cách tạo trên windows

b1: cần cài virtualenv và thêm path đầy đủ

b2: gọi lệnh tạo 1 môi trường ảo: virtualenv -p C:\Python36\python.exe btl

b3: đứng trong thư mục btl: .\Scripts\activate

- Sau đó cd vào thư mục license_plate_recognition
- Chạy các file .inpynb để test hệ thống