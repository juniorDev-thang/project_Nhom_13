import csv
import os

def khoi_tao_file():
    file_path = os.path.join("files", "ds_hoadon.csv")
    if not os.path.exists("files"):
        os.makedirs("files")
    if not os.path.isfile(file_path):
        with open(file_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["MaHD", "TenKhach", "LoaiPhong", "SoGio", "ThanhTien"])

def nhap_hoa_don():
    ds = []
    while True:
        ma = input("Nhập mã hóa đơn: ").strip()
        if ma == "":
            continue
        ten = input("Nhập tên khách: ").strip()
        if ten == "":
            continue
        try:
            loai = int(input("Nhập loại phòng (1: VIP, 2: Thường): "))
            if loai not in [1, 2]:
                continue
        except ValueError:
            continue
        try:
            sogio = int(input("Nhập số giờ hát: "))
            if sogio <= 0:
                continue
        except ValueError:
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