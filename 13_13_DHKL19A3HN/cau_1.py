#Viết hàm kiểm tra số Padovan, tìm số Padovan lớn nhất nhỏ hơn K(dùng comment giải thích thuật toán cho nhóm nhiệm vụ chính là phải nghiên cứu)
'''Câu 1: Hãy viết một chương trình đặt tên là cau_1.py thực hiện các công việc sau: 
a. Viết một hàm kiểm tra một số nguyên dương m có phải là số Padovan hay không? 
(Biết rằng: Dãy số Padovan P(n) được định nghĩa bởi: P(0) = P(1) = P(2) = 1 và P(n) 
= P(n-2) + P(n-3) với n > 2. Các số đầu tiên của dãy là: 1, 1, 1, 2, 2, 3, 4, 5, 7, 9...). 
b. Nhập vào một số nguyên dương K. Hãy liệt kê tất cả các số Padovan nhỏ hơn hoặc 
bằng K. 
'''
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
print("câu a)")
def la_padovan(m):
    if m < 1 :
        return False
    day = day_padovan(m)
    return m in day
try:
    m = int(input("nhập m để kiểm tra (padovan): "))
    if m <1:
        print("số padovan phải >=1")
    else:
        if la_padovan(m):
            print(f"{m} là số padovan")
        else:
            print(f"{m} không phải là số padovan")
except ValueError:
    print("vui lòng nhập số hợp lệ !!!")

#hàm liệt kê dãy padovan nhỏ hơn hoặc bằng K
print("câu b)")
try:
    K = int(input("Nhập số K: "))
    if K < 1:
        print("K phải >=1")
    else:
        day_padovan_nho_hon_K = day_padovan(K)
        tong = len(day_padovan_nho_hon_K)
        print(f"các số padovan nhỏ hơn {K} là:",day_padovan_nho_hon_K)
        print(f"tổng cộng có {tong} padovan ",tong)
except ValueError:
    print("vui lòng nhập số K hợp lệ!!!")
