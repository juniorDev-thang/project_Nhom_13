from libs.thuvien_karaoke import *

def menu():
    khoi_tao_file()
    ds_hoa_don = []
    
    while True:
        print("\n" + "="*60)
        print("\t\tCHƯƠNG TRÌNH QUẢN LÝ QUÁN KARAOKE")
        print("="*60)
        print("1. Nhập thông tin hóa đơn")
        print("2. Tính tiền cho các hóa đơn đã nhập")
        print("3. Lưu hóa đơn vào file CSV")
        print("4. Sắp xếp và hiển thị danh sách")
        print("0. Thoát chương trình")
        print("="*60)
        
        lua_chon = input("Chọn chức năng (0-4): ").strip()
        
        if lua_chon == "1":
            print("\n📝 NHẬP THÔNG TIN HÓA ĐƠN")
            print("="*60)
            ds_moi = nhap_hoa_don()
            if ds_moi:
                ds_hoa_don.extend(ds_moi)
                print(f"\n✅ Đã nhập {len(ds_moi)} hóa đơn")
            else:
                print("\n❌ Không có hóa đơn nào được nhập!")
        
        elif lua_chon == "2":
            print("\n💰 TÍNH TIỀN HÓA ĐƠN")
            print("="*60)
            if not ds_hoa_don:
                print("⚠️ Chưa có hóa đơn! Vui lòng chọn [1] trước")
            else:
                chua_tinh = sum(1 for hd in ds_hoa_don if hd["ThanhTien"] == 0) #- với mỗi hóa đơn thỏa điều kiện, biểu thức trả về số 1
                
               
                if chua_tinh == 0:
                    print("✅ Tất cả hóa đơn đã tính tiền!")
                else:
                    for hd in ds_hoa_don:
                        if hd["ThanhTien"] == 0:
                            tinh_tien(hd)
                    print(f"✅ Đã tính tiền cho {chua_tinh} hóa đơn")
                
                hien_thi(ds_hoa_don)
    
        
        elif lua_chon == "3":
            print("\n💾 LƯU DỮ LIỆU VÀO FILE CSV")
            print("="*60)
            if not ds_hoa_don:
                print("⚠️ Danh sách trống! Không có gì để lưu")
            else:
                chua_tinh = sum(1 for hd in ds_hoa_don if hd["ThanhTien"] == 0)
                
                if chua_tinh > 0:
                    print(f"⚠️ Có {chua_tinh} hóa đơn chưa tính tiền!")
                    xac_nhan = input("Tính tiền trước khi lưu? (y/n): ").lower()
                    if xac_nhan == "y":
                        for hd in ds_hoa_don:
                            if hd["ThanhTien"] == 0:
                                tinh_tien(hd)
                        print("✅ Đã tính tiền xong!")
                    else:
                        print("❌ Vui lòng tính tiền trước khi lưu!")
                        continue
                
                luu_file(ds_hoa_don)
                print(f"✅ Đã lưu {len(ds_hoa_don)} hóa đơn vào files/ds_hoadon.csv")
        
        elif lua_chon == "4":
            print("\n📊 SẮP XẾP VÀ HIỂN THỊ DANH SÁCH")
            print("="*60)
            if not ds_hoa_don:
                print("⚠️ Danh sách trống! Vui lòng chọn [1] trước")
            else:
                chua_tinh = sum(1 for hd in ds_hoa_don if hd["ThanhTien"] == 0)
                
                if chua_tinh > 0:
                    print(f"⚠️ Có {chua_tinh} hóa đơn chưa tính tiền!")
                    print("Sắp xếp sẽ không chính xác. Vui lòng chọn [2] trước\n")
                
                ds_hoa_don = sap_xep(ds_hoa_don)
                print("✅ Đã sắp xếp theo thứ tự giảm dần!\n")
                hien_thi(ds_hoa_don)
        
        elif lua_chon == "0":
            print("="*60)
            if ds_hoa_don:
                chua_luu = any(hd["ThanhTien"] == 0 for hd in ds_hoa_don)
                if chua_luu:
                    print("⚠️ Có dữ liệu chưa được lưu!")
                    xac_nhan = input("Lưu trước khi thoát? (y/n): ").lower()
                    if xac_nhan == "y":
                        for hd in ds_hoa_don:
                            if hd["ThanhTien"] == 0:
                                tinh_tien(hd)
                        luu_file(ds_hoa_don)
                        print("✅ Đã lưu dữ liệu thành công!")
            
            print("👋 Cảm ơn bạn đã sử dụng chương trình!")
            print("Hẹn gặp lại!")
            print("="*60)
            break
        
        else:
            print("❌ Lựa chọn không hợp lệ! Vui lòng chọn 0-4")

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\n⚠️ Chương trình bị ngắt bởi người dùng!")
        print("👋 Tạm biệt!\n")
    except Exception as e:
        print(f"❌ Lỗi không mong muốn: {e}")
        print("📞 Vui lòng liên hệ Nhóm 13 để giải quyết!\n")