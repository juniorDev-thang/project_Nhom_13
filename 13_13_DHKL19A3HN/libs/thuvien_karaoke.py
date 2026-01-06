#=======================================
#Câu 2: Viết chương trình quản lý hóa đơn của một quán Karaoke gồm thông tin: Mã hóa đơn; Tên khách; Loại phòng (1: VIP, 2: Thường); Số giờ hát; Thành tiền. (Thông tin nhập từ bàn phím: Mã, Tên, Loại phòng, Số giờ). 
#I. Trong thư mục libs, viết module thuvien_karaoke.py gồm các hàm: 
#1. Khởi tạo file ds_hoadon.csv trong thư mục files (tạo file và ghi header nếu chưa có). 
#2. Nhập thông tin hóa đơn (trả về danh sách dictionary, chưa tính Thành tiền). 
#3. Tính Thành tiền theo quy tắc: 
#Phòng 1 (VIP): 300.000 VNĐ/giờ. 
#Phòng 2 (Thường): 150.000 VNĐ/giờ. 
#Khuyến mãi: Nếu hát >= 5 giờ: Giảm 20% tổng tiền. Nếu hát >= 5 giờ (và <5): 
#Giảm 10% tổng tiền. 
#4. Lưu danh sách hóa đơn vào file ds_hoadon.csv. 
#5. Sắp xếp danh sách theo thứ tự giảm dần của Thành tiền. 
#6. Hiển thị danh sách ra màn hình. 
# =======================================

# Ý 1,2,3 của Vũ
# Ý 4,5,6 của Nhi
import os
import csv
def khoi_tao_file():
    file_path = os.path.join("files","ds_hoadon.csv") #-  tạo thư mục files\ds_hoadon.csv
    if not os.path.exists("files"): #kiểm tra files tồn tại hay chưa
        os.makedirs("files")  # tạo file nếu chưa có
    if not os.path.isfile(file_path):
        with open(file_path,mode="w",newline="",encoding = "utf-8") as f:
            writer = csv.writer(f)
            #tạo header
            header = ["MaHD","TenKhach","LoaiPhong","SoGio","ThanhTien"]
            writer.writerow(header)
    return file_path
khoi_tao_file()
