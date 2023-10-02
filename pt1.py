
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else:
    x = -b / a
    print("Phương trình có nghiệm:")
    print("x =", x)