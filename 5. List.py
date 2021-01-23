# *** 1. LIST TRONG PYTHON ***
print("1. LIST TRONG PYTHON")
# Có khả năng chứa nhiều phần tử
# Chứa nhiều phần tử khác kiểu dữ liệu
# Cú pháp: var = [value1, value2, value3] 
# Trong đó:
#   + var là tên biến
#   + value1, value2, value3 là giá trị các phần tử
# Ví dụ:
basic_python_lesson = ["B1. Variable", "B2. Print", "B3. String", "B4. Number", "B5. List", "..."]
print("1.1. ", basic_python_lesson)
info = ["Đặng Bình Phước", 21]
print("1.2. ", info)

# *** 2. TRUY CẬP ĐẾN TỪNG PHẦN TỬ ***
print("\n2. TRUY CẬP ĐẾN TỪNG PHẦN TỬ")
# 2.1. Truy cập được đến từng phần tử của list
print("2.1. Truy cập được đến từng phần tử của list")
# List trong python bắt đầu từ vị trí 0
# Cú pháp: var[index]
# Trong đó:
#   + var là tên biến
#   + index là vị trí
# Ví dụ:
basic_python_lesson = ["B1. Variable", "B2. Print", "B3. String", "B4. Number", "B5. List", "..."]
print("2.1.1. ", basic_python_lesson[0])
print("2.1.2. ", basic_python_lesson[2])
print("2.1.3. ", basic_python_lesson[-1])
print("2.1.4. ", basic_python_lesson[-2])
# 2.2. Truy cập được 1 phần của list
print("2.2. Truy cập được 1 phần của list")
# Cú pháp: var[start: end]
# Trong đó:
#   + var là tên biến
#   + start là vị trí bắt đầu lấy list con. Nếu để trống start = 0
#   + end là vị trí kết thúc lấy list con. Nếu để trống end = len(list) -> độ dài của list
# Ví dụ:
basic_python_lesson = ["B1. Variable", "B2. Print", "B3. String", "B4. Number", "B5. List", "..."]
print("2.2.1. ", basic_python_lesson[1: 3])
print("2.2.2. ", basic_python_lesson[-3: ])

# *** 3. SỬA ĐỔI VÀ XOÁ BỎ PHẦN TỬ ***
print("\n3. SỬA ĐỔI VÀ XOÁ BỎ PHẦN TỬ")
# 3.1. Sửa đổi
print("3.1. Sửa đổi")
# Cú pháp : var[index] = value
# Trong đó:
#   + var là tên biến
#   + index là vị trí cần sửa đổi
#   + value là giá trị chuyển đổi thành
# Ví dụ:
basic_python_lesson = ["B1. Variable", "B2. Print", "B3. String", "B4. Number", "B5. List", "..."]
basic_python_lesson[2] = "B3. Chuỗi"
print("3.1.1. ", basic_python_lesson)
# 3.2. Xoá
print("3.2. Xoá")
# Cú pháp : del var[index]
# Trong đó:
#   + var là tên biến
#   + index là vị trí cần sửa đổi
# Ví dụ:
basic_python_lesson = ["B1. Variable", "B2. Print", "B3. String", "B4. Number", "B5. List", "..."]
del basic_python_lesson[2]
print("3.2.1. ", basic_python_lesson)

# *** 4. LIST LỒNG NHAU ***
# Do list chứa được nhiều kiểu dữ liệu nên list có thể chứa được list chứa list chứa list chứa ... =]]
# Ví dụ:
favorite_foods = ["Bún riêu cua", "Gà rán ", "Bánh bao chiên"]
info = ["Đặng Bình Phước", favorite_foods]
print("4.1. ", info)
# Nó cũng có khả năng truy cập từng phần tử đã nêu như trên
print("4.2. ", info[0])
print("4.3. ", info[1])
print("4.4. ", info[1][0])

# Nếu bạn học python với mục đính để làm Machine Learning hoặc Deep Learning
# Bạn nên xem kĩ bài này 
# Vì nó tương tự với 1 số thư viện để làm ML và DL mà chúng ta sử dụng rất nhiều trong quá trình học và làm ML và DL 
# Ví dụ: numpy





