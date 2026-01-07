from libs.thuvien_karaoke import *
def menu():
    khoi_tao_file()
    ds_hoa_don = []
    while True:
        print("\n"+ "="*60)
        print("\t\t CHƯƠNG TRÌNH QUẢN LÝ QUÁN KARAOKE")
        print("="*60)
        print("1.Nhập thông tin hóa đơn")
        print("2.Tính tiền cho các hóa đơn đã nhập")
        print("3.Lưu hóa đơn vào danh sách file CSV")
        print("4.Sắp xếp danh sách hiển thị theo thứ tự giảm dần")
        print("0.Thoát chương trình")

        print("="*60)
        lua_chon = input("Mời bạn chọn các chức năng (0-4): ").strip()
        if lua_chon == "1":
            print("\n NHẬP THÔNG TIN HÓA ĐƠN")
            print("="*60)
            ds_moi = nhap_hoa_don()
            if ds_moi:
                ds_hoa_don.extend(ds_moi)
                print(f"\n Đã nhập thành công {len(ds_moi)} hóa đơn")
            else:
                print("\n Không có hóa đơn nào được nhập!")
        elif lua_chon == "2":
            print("\n TÍNH TIỀN HÓA ĐƠN")
            print("="*60)
            if not ds_hoa_don:
                print("Chưa có hóa đơn nào được nhập! Vui lòng nhập hóa đơn trước khi tính tiền (Gợi ý: Chọn 1 trước)")
            else:
                # đếm số hóa đơn chưa tính tiền
                chua_tinh = sum(1 for hd in ds_hoa_don if hd["ThanhTien"] == 0)
                if chua_tinh == "0":
                    print("Tất cả hóa đơn đã tính tiền!")
                else:
                    for hd in ds_hoa_don:
                        if hd["ThanhTien"] == 0:
                            tinh_tien(hd)
                    print("ĐÃ TÍNH TIỀN CHO HÓA ĐƠN")
            hien_thi(ds_hoa_don)
            break

        elif lua_chon == "3":
            print("\n LƯU DỮ LIỆU VÀO FILE CSV")
            print("="*60)
            if not ds_hoa_don:
                print("Danh sách trống! Không có gì để lưu")
            else:
                #kiểm tra xem tình tiền chưa
                chua_tinh = sum(1 for hd in ds_hoa_don if hd["ThanhTien"] == 0)

                if chua_tinh > 0:
                    print(f"Cảnh báo: Có {chua_tinh} hóa đơn chưa được tính tiền!")
                    xac_nhan = input("Bạn có muốn tính tiền trước khi lưu? (y/n) ").lower()
                    if xac_nhan == "y":
                        for hd in ds_hoa_don:
                            if hd["ThanhTien"] == 0:
                                tinh_tien(hd)
                        print("Đã tính tiền xong!")
                    else:
                        print("Tính tiền mới được vào hát hoặc đi về!")
                        break

                luu_file(ds_hoa_don)
                print(f"Đã lưu {len(ds_hoa_don)} hóa đơn vào files/ds_hoadon.csv")

        elif lua_chon == "4":
            print("\n SẮP XẾP GIẢM DẦN VÀ HIỂN THỊ DANH SÁCH")
            print("="*60)
            if not ds_hoa_don:
                print("Danh sách trống! Vui lòng nhập hóa đơn trước (chọn 1) ")
            else:
                chua_tinh = sum(1 for hd in ds_hoa_don if hd["ThanhTien"] == 0)

                if chua_tinh > 0:
                    print(f"Có {chua_tinh} hóa đơn chưa được tính tiền!")
                    print("sắp xếp sẽ không chính xác. Vui lòng tính tiền trước (chọn 2 \n")
                ds_hoa_don = sap_xep(ds_hoa_don)
                print("Đã sắp xếp hóa đơn theo thứ tự giảm dần của thành tiền!\n")

                hien_thi(ds_hoa_don)


        elif lua_chon == "0":
            print("="*60)
            if ds_hoa_don:
                print("Bạn có dữ liệu chưa được lưu vào file!")
                xac_nhan = input("Bạn có muốn lưu chương trình trước khi thoát? (y/n) ").lower()
                if xac_nhan == "y":
                    for hd in ds_hoa_don:
                        if hd["ThanhTien"] == 0:
                            tinh_tien(hd)
                    luu_file(ds_hoa_don)
                    print(("Bạn đã lưu dữ liệu thành công!"))
            print("Cảm ơn bạn đã sử dụng chương trình!")
            print("Hẹn gặp lại!")
            print("="*60)
            break
        else:
            print("Lựa chọn không hợp lệ!")


        
if __name__=="__main__":
    try:
        menu()
    except  KeyboardInterrupt:
        print("\n\n Chương trình bị ngắt bởi người dùng!")
        print("Tạm biệt!\n")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")
        print("Vui lòng liên hệ nhóm 13 để giải quyết! \n")
