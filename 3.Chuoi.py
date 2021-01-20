# *** 1. Các kí tự đặc biệt trong chuỗi ***
print("1. Các kí tự đặc biệt trong chuỗi")
# " là kí tự đặc biệt do đó nó sẽ báo lỗi trong quá trình biên dịch
# Ví dụ: print("chào mừng bạn đến bài "chuỗi"")
# Để sử dụng được chúng ta sử dụng kí tự \ trước kí tự đặc biệt
print("1.1. chào mừng bạn đến bài \"chuỗi\"")
# Tương tự vậy ta cũng có thể áp dụng với kí tự đặc biệt '
print('1.2. chào mừng bạn đến bài \'chuỗi\'')
# Hoặc sử dụng đối của nó
print('1.3. chào mừng bạn đến bài "chuỗi"')
print("1.4. chào mừng bạn đến bài 'chuỗi'")

# Một số kí tự đặc biệt khác
print("1.5. chào \n mừng bạn đến bài chuỗi")
# \n -> xuống dòng
print("1.6. chào \t mừng bạn đến bài chuỗi")
# \t -> tab
print("1.7. chào \a mừng bạn đến bài chuỗi")
# \a -> chuông cảnh báo
print("1.8. chào \bmừng bạn đến bài chuỗi")
# \b -> xoá bỏ khoảng trắng phía trước nó

# *** Kết thúc phần 1 ***

# *** 2. Format chuỗi ***
print("\n2. Format chuỗi")
# Cú pháp: print("%type" %(binding))
# Trong đó: 
#   + %type là các kiểu dữ liệu mà bạn muốn binding và thay thế vị trí đó
#   + %binding là các giá trị mà bạn muốn binding vào vị trí xác định trong chuỗi
# Cú pháp xem trong "Cú pháp format trong chuỗi"
# Ví dụ:
name = "Đặng Bình Phước"
full = "2.1. Chào bạn %s" %(name)
print(full)

# *** 3. Truy cập đến từng giá trị của chuỗi ***
print("\n3. Truy cập đến từng giá trị của chuỗi")
# Cú pháp: str[index]
# Trong đó: 
#   + str là tên của biến chứa chuỗi
#   + index là vị trí của kí tự trong chuỗi
# Trong python hỗ trợ tuy xuất cả 2 chiều nên:
#   + Tính từ đầu thì index = 0
#   + Tính từ cuối thì index = -1
# Ví dụ:
name = "Đặng Bình Phước"
print("3.1 ", name[0])
print("3.2 ", name[-1])
# Hoặc có thể lấy 1 đoạn trong chuỗi 
# Cú pháp: str[start: end]
# Trong đó:
#   + start là vị trí bắt đầu lấy chuỗi, nếu để trống mặc định start = 0
#   + end là vị trí kết thúc , nếu để trống mặc định end = độ dài chuỗi
# Ví dụ:
name = "Đặng Bình Phước"
print("3.3 ", name[0: 4])
print("3.4 ", name[-5: 15])
print("3.5 ", name[5: ])