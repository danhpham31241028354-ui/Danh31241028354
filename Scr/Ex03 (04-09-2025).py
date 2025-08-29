import random
# Câu 14: Write a Python program to print the numbers of a specified list after removing
# even numbers from it.
def ex14():
    C14 = [1,2,3,4,5,6,7,8,9,10]
    C14_so_le = []
    for i in (C14):
        if i % 2 != 0:
            C14_so_le.append(i)
    print("(Câu 14) Danh sách sau khi được loại bỏ số chẵn là: ",C14_so_le)
#Câu 15: Write a Python program to shuffle and print a specified list.
def ex15():
    C15 = [1,2,3,4,5,6,7,8,9,10,11]
    random.shuffle(C15)
    print("(Câu 15) Danh sách sau khi được xáo trộn là: ",C15)
# Câu 16: Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both
# included).
def ex16():
    C16 = []
    for i in range (1,31):
        C16.append(i**2)
        KQ_cuoi_cung = C16[:5] + C16[-5:]
    print("Danh sách chỉ gồm 5 số đầu và 5 số cuối là: ",KQ_cuoi_cung)
def ex17():
    C17_1 = [1,2,3,4,5,6,7,8,9,10]
    C17_2 = [2,4,6,8,10,12]
    different_1 = []
    different_2 = []
    for i in C17_1:
        if i not in C17_2:
            different_1.append(i)
    print("Các phần tử có trong list 1 nhưng có trong list 2 là: ",different_1)
    for i in C17_2:
        if i not in C17_1:
            different_2.append(i)
    print("Các phần tử có trong list 2 nhưng có trong list 1 là: ", different_2)
def ex21():
    C21 = ["D","A","N","H"]
    print("Chuỗi sau tạo là: ","".join(C21))



ex21()