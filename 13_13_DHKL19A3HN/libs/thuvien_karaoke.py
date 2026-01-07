# module
'''
Viết chương trình quản lý hóa đơn của một quán Karaoke gồm thông tin: Mã 
hóa đơn; Tên khách; Loại phòng (1: VIP, 2: Thường); Số giờ hát; Thành tiền. (Thông 
tin nhập từ bàn phím: Mã, Tên, Loại phòng, Số giờ). 
I. Trong thư mục libs, viết module thuvien_karaoke.py gồm các hàm: 
1. Khởi tạo file ds_hoadon.csv trong thư mục files (tạo file và ghi header nếu 
chưa có). 
2. Nhập thông tin hóa đơn (trả về danh sách dictionary, chưa tính Thành tiền).  
3. Tính Thành tiền theo quy tắc: 
Phòng 1 (VIP): 300.000 VNĐ/giờ. 
Phòng 2 (Thường): 150.000 VNĐ/giờ. 
Khuyến mãi: Nếu hát >= 5 giờ: Giảm 20% tổng tiền. Nếu hát >= 5 giờ (và <5): 
Giảm 10% tổng tiền. 
4. Lưu danh sách hóa đơn vào file ds_hoadon.csv. 
5. Sắp xếp danh sách theo thứ tự giảm dần của Thành tiền. 
6. Hiển thị danh sách ra màn hình. 

'''
import os
import csv
# 1
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
        print(f"đã tạo file mới {file_path}")
    return file_path

# 2
def nhap_hoa_don():
    # nhập vào list trả về dict
    ds = []

    while True:
        print("---NHẬP HÓA ĐƠN MỚI---")
        # Nhập mã hóa đơn
        ma = input("Nhập mã hóa đơn: ").strip()
        if ma == "":
            print("Mã hóa đơn không được để trống, vui lòng nhập lại!")
            continue
        # Nhập tên khách
        ten = input("Nhập tên khách: ").strip()
        if ten == "":
            print("Tên khách hàng không được để trống, vui lòng nhập lại!")
            continue
        # Chọn phòng
        print("Chọn loại phòng: ")
        print("Phòng 1 (VIP): 300.000 VNĐ/giờ.")
        print("Phòng 2 (Thường): 150.000 VNĐ/giờ.")
        phong = [1,2]
        try:
            loaiphong = int(input("Nhập loại phòng (1 hoặc 2): "))
            if loaiphong not in phong:
                print("Chỉ được nhập loại phòng 1 hoặc 2!")
                continue
        except ValueError:
            print("Loại phòng phải là số nguyên (vd: 1,2)")
            continue
        # Giờ hát
        try:
            sogio = int(input("Nhập số giờ hát: "))
            if sogio <= 0:
                print("Số giờ hát phải > 0!")
                continue
        except ValueError:
            print("Số giờ hát phải là số nguyên (vd: 1,2,3......)")
            continue
        ds.append({
            "MaHD":ma,
            "TenKhach":ten,
            "LoaiPhong":loaiphong,
            "SoGio":sogio,
            "ThanhTien":0
        })
        hoadon_tiep = input("Bạn có muốn nhập thêm hóa đơn không? (y/n): ").lower()
        if hoadon_tiep == "n": # nếu y thì hóa đơn sẽ lặp lại vì mình dùng while True:
            break
    return ds
#3   
def tinh_tien(hoadon):
    #lấy thông tin LoaiPhong và SoGio
    LoaiPhong = hoadon["LoaiPhong"]
    sogio = hoadon["SoGio"]
    #phân loại phòng tình tiền
    p1 = 300000
    p2 = 150000
    if LoaiPhong == 1:
        gia = p1
    else:
        gia = p2
    tinhtien = gia * sogio
    # giảm giá
    if sogio >= 5:
        tinhtien *= 0.8
    elif sogio < 5:
        tinhtien *= 0.9
    hoadon["ThanhTien"] = int(tinhtien)
    return hoadon
#4
def luu_file(ds):
    # tạo lại file cho chắc chắn nếu có rồi not sẽ bỏ qua =))
    file_path = os.path.join("files","ds_hoadon.csv") #-  tạo thư mục files\ds_hoadon.csv
    if not os.path.exists("files"): #kiểm tra files tồn tại hay chưa
        os.makedirs("files")
    with open(file_path,mode="w",newline="",encoding = "utf-8") as f:
        writer = csv.writer(f)
        #tạo header
        header = ["MaHD","TenKhach","LoaiPhong","SoGio","ThanhTien"]
        writer.writerow(header)
        # phần chính lưu dữ liệu
        for hd in ds:
            writer.writerow([ # ghi hàng theo list /tuple
                hd["MaHD"],
                hd["TenKhach"],
                hd["LoaiPhong"],
                hd["SoGio"],
                hd["ThanhTien"]
            ])

#5
def sap_xep(ds): # giảm dần
    return sorted(ds,key=lambda x: x["ThanhTien"],reverse=True)
    
#6
def hien_thi(ds):
    # nếu không có gì trong csv
    if not ds:
        print("Danh sách trống!")
        return 0

    # tiêu đề bảng
    print("{:<10} {:<20} {:<10} {:<10} {:<15}".format("MaHD","TenKhach","LoaiPhong","SoGio","ThanhTien"))
    print("="*70)

    for hd in ds:
        if hd["LoaiPhong"] == 1:
            Loai_Phong = "VIP"
        else:
            Loai_Phong = "Thường"

        print("{:<10} {:<20} {:<10} {:<10} {:<15,} VND".format(
            hd["MaHD"], hd["TenKhach"], Loai_Phong, hd["SoGio"], hd["ThanhTien"]
        ))

    print("="*70)
    print(f"Tổng số hóa đơn là: {len(ds)}")
    print(f"Tổng doanh thu là: {sum(hd['ThanhTien'] for hd in ds):,} VND")
# tạo thêm hàm cho kiểm tra bài tét bắt lỗi tạo file nếu có 
def doc_file():
    file_path = os.path.join("files","ds_hoadon.csv")
    ds = []
    try: 
        if os.path.isfile(file_path):
            with open(file_path, mode="r",newline="",encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for hang in reader:
                    ds.append({
                        "MaHD":hang["MaHD"],
                        "TenKhach":hang["TenKhach"],
                        "LoaiPhong":int(hang["LoaiPhong"]),
                        "SoGio":int(hang["SoGio"]),
                        "ThanhTien":int(hang["ThanhTien"])
                    })
            print(f"đã đọc {len(ds)} hóa đơn từ file")
        else:
            print("File chưa tồn tại")
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
    return ds
