import csv
import os

def khoi_tao_file():
    filename = "ds_hoadon.csv"
    if not os.path.exists(filename):
        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["MaHD", "TenKH", "SoLuong", "DonGia", "ThanhTien"])

def luu_file(ds):
    filename = "ds_hoadon.csv"
    with open(filename, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for hd in ds:
            writer.writerow([hd["MaHD"], hd["TenKhach"], hd["LoaiPhong"], hd["SoGio"], hd["ThanhTien"]])

def sap_xep(ds):
    return sorted(ds, key=lambda x: x["ThanhTien"], reverse=True)