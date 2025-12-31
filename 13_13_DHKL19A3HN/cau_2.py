<<<<<<< HEAD
from libs.thuvien_karaoke import Nhap_Hoa_Don

ds = Nhap_Hoa_Don()
print(ds)
=======
#Thành viên 3: Đỗ Ngọc Anh
#Làm Menu và Hiển thị:
#Xử lý menu , import module ,gọi hàm,hiển thị danh sách
from libs.thuvien_karaoke import *

def menu():
    khoi_tao_file()
    # Biến lưu trữ danh sách hóa đơn đang xử lý trong phiên làm việc
    ds_hien_tai = []

    while True:
        print("\n--- QUẢN LÝ QUÁN KARAOKE ---")
        print("1. Nhập và tính tiền hóa đơn mới")
        print("2. Sắp xếp danh sách (Giảm dần Thành tiền)")
        print("3. Lưu dữ liệu vào file CSV")
        print("4. Hiển thị danh sách hiện tại")
        print("0. Thoát chương trình")
        
        chon = input("Mời bạn chọn chức năng: ")

        if chon == "1":
            moi = nhap_thong_tin()
            if moi:
                ds_hien_tai.extend(tinh_thanh_tien(moi))
                print(">> Đã nhập và tính tiền thành công!")
                hien_thi_danh_sach(ds_hien_tai)
        
        elif chon == "2":
            if ds_hien_tai:
                ds_hien_tai = sap_xep_giam_dan(ds_hien_tai)
                print(">> Đã sắp xếp danh sách!")
                hien_thi_danh_sach(ds_hien_tai)
            else:
                print("!! Chưa có dữ liệu để sắp xếp.")

        elif chon == "3":
            if ds_hien_tai:
                luu_file(ds_hien_tai)
                print(f">> Đã lưu vào {FILE_PATH} thành công!")
            else:
                print("!! Danh sách trống, không có gì để lưu.")

        elif chon == "4":
            if ds_hien_tai:
                hien_thi_danh_sach(ds_hien_tai)
            else:
                print("!! Danh sách hiện đang trống.")

        elif chon == "0":
            print("Tạm biệt! Chúc bạn một ngày tốt lành.")
            break
        else:
            print("!! Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    menu()
>>>>>>> origin/NgocAnh
