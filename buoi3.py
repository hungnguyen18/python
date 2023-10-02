import math

a = int(input("nhap so a: "))


def sum(a: float, b: float):
    return a + b


def minus(a: float, b: float):
    return a - b


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def pt2(a: float, b: float, c: float):
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


def bang_cuu_chuong(a: int):
    if not (a > 1 and a <= 10):
        return
    for i in range(1, 11):
        print(a, "*", i, "=", a * i)


# bang_cuu_chuong(a)


g = 5


def d():
    # global g
    # g = 2
    g = g + 1


d()
print(g)
