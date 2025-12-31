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



import csv
import os
#1
def khoi_tao_file():
    file_path = os.path.join("files", "ds_hoadon.csv")
    if not os.path.exists("files"):
        os.makedirs("files")
    if not os.path.isfile(file_path):
        with open(file_path, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["MaHD", "TenKhach", "LoaiPhong", "SoGio", "ThanhTien"])
#2
def nhap_hoa_don():
    ds = []
    while True:
        ma = input("Nhập mã hóa đơn: ").strip()
        if ma == "":
            print(" Mã hóa đơn không được để trống!")
            continue

        ten = input("Nhập tên khách: ").strip()
        if ten == "":
            print(" Tên khách không được để trống!")
            continue

        # Hỏi loại phòng rõ ràng hơn
        print("Chọn loại phòng:")
        print("1. VIP (300.000 VNĐ/giờ)")
        print("2. Thường (150.000 VNĐ/giờ)")
        try:
            loai = int(input("Nhập loại phòng (1 hoặc 2): "))
            if loai not in [1, 2]:
                print(" Loại phòng chỉ được nhập 1 hoặc 2!")
                continue
        except ValueError:
            print(" Loại phòng phải là số nguyên!")
            continue

        try:
            sogio = int(input("Nhập số giờ hát: "))
            if sogio <= 0:
                print(" Số giờ hát phải > 0!")
                continue
        except ValueError:
            print(" Số giờ hát phải là số nguyên!")
            continue

        ds.append({
            "MaHD": ma,
            "TenKhach": ten,
            "LoaiPhong": loai,
            "SoGio": sogio,
            "ThanhTien": 0
        })

        tiep = input("Bạn có muốn nhập thêm hóa đơn? (y/n): ").lower()
        if tiep != "y":
            break
    return ds
#3
def tinh_tien(hoadon):
    loai = hoadon["LoaiPhong"]
    sogio = hoadon["SoGio"]
    gia = 300000 if loai == 1 else 150000
    tong = gia * sogio
    if sogio >= 5:
        tong *= 0.8
    elif sogio >= 3:
        tong *= 0.9
    hoadon["ThanhTien"] = int(tong)
    return hoadon
#4
def luu_file(ds):
    file_path = os.path.join("files", "ds_hoadon.csv")
    with open(file_path, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for hd in ds:
            writer.writerow([
                hd["MaHD"],
                hd["TenKhach"],
                hd["LoaiPhong"],
                hd["SoGio"],
                hd["ThanhTien"]
            ])
#5
def sap_xep(ds):
    return sorted(ds, key=lambda x: x["ThanhTien"], reverse=True)
#6
def hien_thi(ds):
    print("{:<10} {:<20} {:<10} {:<10} {:<15}".format("MaHD", "TenKhach", "LoaiPhong", "SoGio", "ThanhTien"))
    for hd in ds:
        print("{:<10} {:<20} {:<10} {:<10} {:<15}".format(
            hd["MaHD"], hd["TenKhach"], hd["LoaiPhong"], hd["SoGio"], hd["ThanhTien"]
        ))