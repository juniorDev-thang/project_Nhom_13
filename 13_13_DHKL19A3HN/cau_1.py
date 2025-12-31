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
def la_padovan(m):
    day = day_padovan(m) # sinh dãy đến khi >=m
    return m in day      # kiểm tra x có trong dãy padovan không

K = int(input("nhập số K:"))
m = int(input("nhập số cần kiểm tra:"))
if la_padovan(m):
    print(m,"là số padovan")
else:
    print(m,"không phải là số padovan")
#hàm liệt kê dãy padovan nhỏ hơn hoặc bằng K
day_padovan_nho_hon_K = day_padovan(K)
print("các số padovan nhỏ hơn hoăc bằng K là :",day_padovan_nho_hon_K)
       
    