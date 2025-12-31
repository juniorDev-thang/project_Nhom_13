import csv
import os

def khoi_tao_file():
    file_path = os.path.join("files", "ds_hoadon.csv")
    if not os.path.exists("files"):
        os.makedirs("files")
    if not os.path.isfile(file_path):
        with open(file_path, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["MaHD", "TenKhach", "LoaiPhong", "SoGio", "ThanhTien"])

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

def sap_xep(ds):
    return sorted(ds, key=lambda x: x["ThanhTien"], reverse=True)

def hien_thi(ds):
    print("{:<10} {:<20} {:<10} {:<10} {:<15}".format("MaHD", "TenKhach", "LoaiPhong", "SoGio", "ThanhTien"))
    for hd in ds:
        print("{:<10} {:<20} {:<10} {:<10} {:<15}".format(
            hd["MaHD"], hd["TenKhach"], hd["LoaiPhong"], hd["SoGio"], hd["ThanhTien"]
        ))