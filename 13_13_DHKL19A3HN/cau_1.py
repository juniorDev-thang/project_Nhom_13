#Viết hàm kiểm tra số Padovan, tìm số Padovan lớn nhất nhỏ hơn K(dùng comment giải thích thuật toán cho nhóm nhiệm vụ chính là phải nghiên cứu)

#hàm sinh dãy padovan đến giới hạn 
def day_padovan(gioi_han): 
    day = [1,1,1] # 3 số padovan đầu tiên
    while True :
        so_padovan_moi = day[-2] + day[-3] # công thức padovan p(n) = p(n-2)+p(n-3)
        if so_padovan_moi > gioi_han:       # nếu vượt quá giới hạn thì dừng
            break    
        day.append(so_padovan_moi)   # thêm số padovan vào cuối danh sách
    return day            
#hàm kiểm tra 1 số có phải là padovan hay không
def la_padovan(x):
    day = day_padovan(x) # sinh dãy đến khi >=x
    return x in day      # kiểm tra x có trong dãy padovan không
#hàm tính số padovan lớn nhất nhỏ hơn K
def padovan_lon_nhat_nho_hon_K(K):
    day = day_padovan(K)  # sinh dãy đến khi vượt quá K
    return day[-1]        # Lấy số cuối cùng trong dãy
K = int(input("nhập số K:"))
x = int(input("nhập số cần kiểm tra:"))
if la_padovan(x):
    print(x,"là số padovan")
else:
    print(x,"không phải là số padovan")
ket_qua = padovan_lon_nhat_nho_hon_K(K)
print("số padovan lớn nhất nhỏ hơn K là:",ket_qua)
    