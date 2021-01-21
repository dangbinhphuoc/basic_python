# *** 1. Kiểu dữ liệu số ***
# Về mặt lưu trữ, 1 biến trong python được khai báo thì:
#   + Nó tạo ra ô lưu trữ cho giá trị đó
#   + Khi gán giá trị mới thì thì nó lại tạo ra ô nhớ mới để lưu trữ
# Trong python hỗ trợ 3 kiểu dữ liệu dạng number
#   + int : kiểu số nguyên (không giới hạn)
#   + float : kiểu số thực 
#   + complex : kiểu số phức
# Để giải phóng vùng nhớ của biến
# Cú pháp: del bien
# Trong đó:
#   + bien là biến cần giải phóng
# Ví dụ:
name = "Đặng Bình Phước"
print("1.1. ", end="") 
print(name)

'''
del name
print("1.2. ", end="")fv
print(name)
'''

# *** 2. Ép kiểu số ***
print("\n2. Ép kiểu số")
# Cú pháp: kieudulieu(bien)
# Trong đó:
#   + kieudulieu : là kiểu dữ liệu muốn chuyển thành
#   + bien : biến dữ liệu muốn được ép kiểu
# Ví dụ:
point = 9.3
print("2.1. ", point, " -> ", int(point))

# *** 3. Các toán tử ***
print("\n3. Các toán tử")
a = 5
b = 2
# Cộng (+)
print("3.1 ", a, " + ", b, " = ", a + b)
# Trừ (-)
print("3.1 ", a, " - ", b, " = ", a - b)
# Nhân (*)
print("3.1 ", a, " * ", b, " = ", a * b)
# Chia (/)
print("3.1 ", a, " / ", b, " = ", a / b)
# Lấy dư (%)
print("3.1 ", a, " % ", b, " = ", a % b)
