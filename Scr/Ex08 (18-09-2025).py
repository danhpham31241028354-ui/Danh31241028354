# ▸Write a Python program:
# 1.to handle a ZeroDivisionError exception when dividing a number by zero.
a = int(input("Câu 1 - Nhập một số nguyên a bất kỳ: "))
b = int(input("Nhập một số nguyên b bất kỳ: "))
try:
    c = a/b
except ZeroDivisionError:
    print("Không thể chia hết cho 0")
else:
    print(c)
# 2.that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    d = int(input("Câu 2 - Nhập một số nguyên d bất kỳ: "))
except ValueError:
    print(f"Giá trị bạn vừa nhập không phải là số nguyên")
# 3.that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
try:
    g = input("Câu 3 - Nhập một số bất kỳ thứ nhất: ")
    f = input("Câu 3 - Nhập một số bất kỳ thứ hai: ")
    if not(g.isdigit() and f.isdigit()):
        raise TypeError("Lỗi. Bạn phải nhập số")
    print("Tổng: ",int(g)+int(f))
except TypeError as e:
    print(e)
# 4.that executes an operation on a list and handles an IndexError exception if the index is out of range.
try:
    C4_list = [1,2,3,4,5]
    n = int(input("Câu 4 - Hãy nhập một vị trí mà bạn muốn in số đó ra từ danh sách: "))
    print(C4_list[n])
except IndexError:
    print("Lỗi index. Phần tử đó không có trong danh sách")
else:
    print("Phần tử bạn muốn in ra là: ",C4_list[n])
# 5.that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
try:
    m = int(input("Hãy nhập một số: "))
except KeyboardInterrupt:
    print("\nLỗi: Bạn đã hủy việc nhập dữ liệu")
# 6.that executes division and handles an ArithmeticError (Lỗi số học) exception if there is an arithmetic error.
try:
    r = 2025
    p = 0
    q = r/p
except ArithmeticError:
    print("Câu 6 - Lỗi số học")

