# 1.Write a Python function to find the maximum of three numbers.
def maxbaso(*args:float):
    m = args[0]
    for x in args:
        if x > m:
            m = x
    return m
so_lon_nhat = maxbaso(1.27272,2.5,2025)
print(f"Câu 1 - Số lớn nhất trong ba số đó là: {so_lon_nhat} ")
# 2.Write a Python function to sum all the numbers in a list.
def tong(*args:float):
    tong = 0
    for x in args:
        tong += x
    return tong
tong_danh_sach = tong(25.25,24.2727,3038)
print(f"Câu 2 - Tổng của danh sách đó là: {tong_danh_sach} ")
# 3.Write a Python program to reverse a string.
def ex03():
    C3 = input("Câu 3 - Hãy nhập một chuỗi: ")
    C3_dao_chuoi = "".join(reversed(C3))
    print(f"Chuỗi {C3} sau khi đảo là: {C3_dao_chuoi}")
ex03()
# 4.Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(n:int):
    if n == 0:
        return 1
    ket_qua = 1
    for i in range(1,n+1):
        ket_qua *= i
    return ket_qua
n = int(input("Câu 4 - Hãy nhập một số mà bạn muốn tính giai thừa của nó: "))
print(f"Giai thừa của số {n} là {factorial(n)}")
# 5.Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
def prime_number(n:int):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
n = int(input("Câu 5 - Hãy nhập một số nguyên n: "))
if prime_number(n):
    print(f"Số {n} là số nguyên tố")
else:
    print(f"Số {n} không là số nguyên tố")
# 6.Write a Python function to print
# 1.all prime numbers that less than a number (enter prompt keyboard).
# 2.the first N prime numbers
# 7.Write a Python function to check whether a number is "Perfect" or not. Then print all perfect number that less than 1000.
# 8.Write a Python function to check whether a string is a pangram or not.
# (Note : Pangrams are words or sentences containing every letter of the alphabet at least once. For example : "The quick brown fox jumps over the lazy dog"