# Hàm tìm số lớn nhất
def find_max(a, b, c):
    max = a
    if max < b: max = b
    if max < c: max = c
    return max
 
 

print("Nhập vào số thứ nhất: ")
a = float(input())
 
print("Nhập vào số thứ hai: ")
b = float(input())
 
print("Nhập vào số thứ ba: ")
c = float(input())
 
 
print("Số lớn nhất trong ba số ", a, " ", b, " ", c, " là ", find_max(a, b, c))

# 2.
max_va = max(a, b, c)
min_va = min(a, b, c)
print(f"Maximum value: {max_va}")
print(f"Minimum value: {min_va}")

sorted_va = sorted([a, b, c])
print(f"Giá trị theo thứ tự tăng dần: {sorted_va}")