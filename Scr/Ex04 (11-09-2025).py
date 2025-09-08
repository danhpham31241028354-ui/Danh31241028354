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
# a. all prime numbers that less than a number (enter prompt keyboard).
def prime_less_than_n():
    prime = []
    for i in range(2,n):
        if prime_number(i):
            prime.append(i)
    return prime
n = int(input("Câu 6a - Hãy nhập một số nguyên n: "))
print(f"Các số nguyên tố nhỏ hơn {n} là: {prime_less_than_n()}")
# b. the first N prime numbers
def first_N_prime():
    first_prime = []
    count = 0
    num = 2
    while count < N:
        if prime_number(num):
            first_prime.append(num)
            count+=1
        num+=1
    return first_prime
N = int(input("Câu 6b - Hãy nhập số lượng số nguyên tố cần in: "))
# 7.Write a Python function to check whether a number is "Perfect" or not.  Then print all perfect number that less than 1000.
def so_hoan_hao(n:int):
    tong_uoc = 0
    for i in range(1,n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n
print(so_hoan_hao(6))
print(so_hoan_hao(1000))
def so_hoan_hao_be_hon_1000():
    SHH_be_hon_1000 = []
    for num in range(2,1000):
        if so_hoan_hao(num):
            SHH_be_hon_1000.append(num)
    return SHH_be_hon_1000
print(f"Câu 7 - Các số hoàn hảo bé hơn 1000 là: {so_hoan_hao_be_hon_1000()} ")
# 8.Write a Python function to check whether a string is a pangram or not.
# (Note : Pangrams are words or sentences containing every letter of the alphabet at least once. For example : "The quick brown fox jumps over the lazy dog"
import string
def is_pangram(text):
    alphabet = set(string.ascii_lowercase) #Lấy tất cả các chữ cái trong bảng chữ cái tiếng Anh
    letters = set(text.lower()) #Chuyển toàn bộ chuỗi về chữ thường, lấy thành set (bộ ký tự duy nhất)
    return alphabet.issubset(letters) #Kiểm tra xem alphabet có nằm trong letters không
print(is_pangram("Câu 8 - The quick brown fox jumps over the lazy dog"))