a = int(input("nhap so a: "))

# if ( not a%2) :
#     print(a, 'la so chan')
# else:
#     print(a, 'la so le')


# def is_leap_year(year: int) -> str:
#     return'nam nhuan' if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 'nam ko nhuan'

# print(is_leap_year(a))


# def calcWater(mass: float) -> float:
#     b = 6.8 + ((mass - 10) * 8.4) if mass > 10 else 6.8
#     return mass * b


# print(calcWater(a))


# def calcPoint(point: float):
#     if point >= 9:
#         print("loai a")
#     elif point >= 7 and point < 9:
#         print("loai b")
#     elif point >= 5 and point < 7:
#         print("loai c")
#     else:
#         print("loai d")


# print(calcPoint(a))


# for i in range(1, 10):
#     if not (i == 4 or i == 5 or i == 8):
#         print(i)


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


print(is_prime(a))
