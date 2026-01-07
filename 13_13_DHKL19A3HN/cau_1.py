'''Câu 1: Hãy viết một chương trình đặt tên là cau_1.py thực hiện các công việc sau: done
a. Viết một hàm kiểm tra một số nguyên dương m có phải là số Padovan hay không? 
(Biết rằng: Dãy số Padovan P(n) được định nghĩa bởi: P(0) = P(1) = P(2) = 1 và P(n) 
= P(n-2) + P(n-3) với n > 2. Các số đầu tiên của dãy là: 1, 1, 1, 2, 2, 3, 4,  75,, 9...). 

b. Nhập vào một số nguyên dương K. Hãy liệt kê tất cả các số Padovan nhỏ hơn hoặc 
bằng K. 

'''

#cong thuc padovan
def day_padovan(gioi_han):
    # khởi tọa dãy số đầu tiên
    day = [1,1,1]
    while True:
        so_padovan_moi = day[-2] + day[-3] # theo công thức đề bài P(0) = P(1) = P(2) = 1 và P(n) = P(n-2) + P(n-3) với n > 2
        if so_padovan_moi > gioi_han: # lớn hơn số truyền vào thì kết thúc
            break
        day.append(so_padovan_moi) # thêm số padovan mới thỏa mãn vào cuối
    return day
 # kiểm tra Dương và Là số padovan hay không
def la_padovan(m):
    if m < 1 :
        return False
    day = day_padovan(m) #kiểm tra m có trong dãy hay không
    return m in day

# câu a}
print("="*40,"\n")
print("Câu a)")
try:
    m = int(input("Nhập số m để kiểm tra (padovan): "))
    if m < 1 :
        print("số padovan phải >= 1\n")
    else:
        if la_padovan(m): 
            print(f"{m} là số padovan chính hiệu!\n")
        else:
            print(f"{m} là không phải là số padovan.\n")
except ValueError:
    print("Vui lòng nhập số nguyên dương hợp lệ!!!! (ví dụ 1,2,3...)\n")
print("="*40,"\n")
print("câu b)")
# câu b
try:
    k = int(input("Nhập số K để liệt kê dãy padovan: "))
    if k < 1:
        print("số padovan phải >= 1")
    else:
        liet_ke_day_padovan_ThoaMan = day_padovan(k)
        tong = len(liet_ke_day_padovan_ThoaMan)
        print(f"các số padovan nhỏ hơn hoặc bằng {k} là: ")
        print(liet_ke_day_padovan_ThoaMan)
        print(f"tổng cộng có {tong} số padovan!\n")
        print("="*40,"\n")


except ValueError:
    print("Vui lòng nhập số nguyên dương hợp lệ!!!! (ví dụ 1,2,3...)")
finally:
    print("Then Kiu!")

