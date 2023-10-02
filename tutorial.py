try:
    # Mã nguồn có thể gây ra ngoại lệ
    num1 = int(input("Nhập số thứ nhất: "))
    num2 = int(input("Nhập số thứ hai: "))

    # Thực hiện phép chia
    result = num1 / num2

    # In kết quả
    print("Kết quả: ", result)

except ValueError:
    print("Lỗi: Không thể chuyển đổi thành số nguyên.")

except ZeroDivisionError:
    print("Lỗi: Số chia phải khác không.")

except Exception as e:
    print("Lỗi không xác định:", str(e))