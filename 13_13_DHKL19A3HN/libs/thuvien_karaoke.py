# module quản lý karaoke 
import os
import csv

# 1. Khởi tạo file
def khoi_tao_file():
    file_path = os.path.join("files","ds_hoadon.csv")
    if not os.path.exists("files"):
        os.makedirs("files")
    if not os.path.isfile(file_path):
        with open(file_path,mode="w",newline="",encoding="utf-8") as f:
            writer = csv.writer(f)
            header = ["MaHD","TenKhach","LoaiPhong","SoGio","ThanhTien"]
            writer.writerow(header)
        print(f"Đã tạo file mới {file_path}")
    return file_path

# 2. Nhập hóa đơn
def nhap_hoa_don():
    ds = []
    while True:
        print("\n---NHẬP HÓA ĐƠN MỚI---")
        
        # Nhập mã hóa đơn
        ma = input("Nhập mã hóa đơn: ").strip()
        if ma == "":
            print("Mã hóa đơn không được để trống!")
            continue
        
        # Nhập tên khách
        ten = input("Nhập tên khách: ").strip()
        if ten == "":
            print("Tên khách không được để trống!")
            continue
        
        # Chọn phòng
        print("Phòng 1 (VIP): 300.000 VNĐ/giờ")
        print("Phòng 2 (Thường): 150.000 VNĐ/giờ")
        try:
            loaiphong = int(input("Nhập loại phòng (1 hoặc 2): "))
            if loaiphong not in [1, 2]:
                print("Chỉ được nhập 1 hoặc 2!")
                continue
        except ValueError:
            print("Loại phòng phải là số nguyên!")
            continue
        
        # Số giờ hát
        try:
            sogio = int(input("Nhập số giờ hát: "))
            if sogio <= 0:
                print("Số giờ phải > 0!")
                continue
        except ValueError:
            print("Số giờ phải là số nguyên!")
            continue
        
        ds.append({
            "MaHD": ma,
            "TenKhach": ten,
            "LoaiPhong": loaiphong,
            "SoGio": sogio,
            "ThanhTien": 0
        })
        
        tiep = input("Nhập thêm hóa đơn? (y/n): ").lower()
        if tiep != "y":
            break
    return ds

# 3. Tính tiền 
def tinh_tien(hoadon):
    loai = hoadon["LoaiPhong"]
    sogio = hoadon["SoGio"]
    
    # Giá phòng
    gia = 300000 if loai == 1 else 150000
    tinhtien = gia * sogio
    
    # Giảm giá 
    if sogio >= 5:
        tinhtien *= 0.8  # Giảm 20%
    elif sogio >= 3: 
        tinhtien *= 0.9  # Giảm 10%
    # Dưới 3 giờ: không giảm
    
    hoadon["ThanhTien"] = int(tinhtien)
    return hoadon

# 4. Lưu file
def luu_file(ds):
    file_path = os.path.join("files","ds_hoadon.csv")
    if not os.path.exists("files"):
        os.makedirs("files")
    
    with open(file_path,mode="w",newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        header = ["MaHD","TenKhach","LoaiPhong","SoGio","ThanhTien"]
        writer.writerow(header)
        
        for hd in ds:
            writer.writerow([
                hd["MaHD"],
                hd["TenKhach"],
                hd["LoaiPhong"],
                hd["SoGio"],
                hd["ThanhTien"]
            ])

# 5. Sắp xếp giảm dần
def sap_xep(ds):
    return sorted(ds, key=lambda x: x["ThanhTien"], reverse=True)

# 6. Hiển thị danh sách
def hien_thi(ds):
    if not ds:
        print("Danh sách trống!")
        return
    
    print("\n{:<10} {:<20} {:<12} {:<10} {:<15}".format(
        "MaHD","TenKhach","LoaiPhong","SoGio","ThanhTien"))
    print("="*70)
    
    for hd in ds:
        loai_text = "VIP" if hd["LoaiPhong"] == 1 else "Thường"
        print("{:<10} {:<20} {:<12} {:<10} {:<15,} VND".format(
            hd["MaHD"], 
            hd["TenKhach"], 
            loai_text, 
            hd["SoGio"], 
            hd["ThanhTien"]
        ))
    
    print("="*70)
    print(f"Tổng số hóa đơn: {len(ds)}")
    print(f"Tổng doanh thu: {sum(hd['ThanhTien'] for hd in ds):,} VND")

# Bonus: Đọc file nhóm tự thêm nếu có nhu cầu sử dụng
def doc_file():
    file_path = os.path.join("files","ds_hoadon.csv")
    ds = []
    try:
        if os.path.isfile(file_path):
            with open(file_path, mode="r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for hang in reader:
                    ds.append({
                        "MaHD": hang["MaHD"],
                        "TenKhach": hang["TenKhach"],
                        "LoaiPhong": int(hang["LoaiPhong"]),
                        "SoGio": int(hang["SoGio"]),
                        "ThanhTien": int(hang["ThanhTien"])
                    })
            print(f"Đã đọc {len(ds)} hóa đơn từ file")
        else:
            print("File chưa tồn tại")
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
    return ds