# Nhập số a, b và kiểm tra điều kiện khác 0
a = float(input("enter a: "))
while True:
    if a == 0:
        a = float(input("a phai khac 0, nhap lai: "))
    else:
        break
    
b = float(input(" nhập hệ số b: "))
while True:
    if b == 0:
        b = float(input(" b phải khác 0,nhập lại số b: "))
    else:
        break
    
# Nhập số c
c = float(input("nhập hệ số c: "))

# Tính Delta
delta = b**2 - 4 * a * c

# Tìm nghiệm của phương trình
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép x1 = x2 = ", -(b / (2 * a)) )
else:
    print("Phương trình có hai nghiệm phân biệt:")
    print("x1 = ", (-(b) + math.sqrt(delta))/(2*a) )
    print("x2 = ", (-(b) - math.sqrt(delta))/(2*a) )