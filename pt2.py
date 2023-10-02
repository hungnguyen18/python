import math

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))


delta = b**2 - 4 * a * c

if delta > 0:
    sqrt_delta = math.sqrt(delta)

    x1 = (-b + sqrt_delta) / (2 * a)
    x2 = (-b - sqrt_delta) / (2 * a)

    print("Phương trình có hai nghiệm phân biệt:")
    print("x1 =", x1)
    print("x2 =", x2)
elif delta == 0:
    x = -b / (2 * a)
    print("Phương trình có nghiệm kép:")
    print("x =", x)
else:
    print("Phương trình vô nghiệm.")
