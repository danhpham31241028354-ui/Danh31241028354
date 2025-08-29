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
def ex19():
    C19_1 = [1,2,3,4,5,6,7,8,9,10]
    C19_2 = [2,4,6,8,10,12]
    different_1 = []
    different_2 = []
    for i in C19_1:
        if i not in C19_2:
            different_1.append(i)
    print("Các phần tử có trong list 1 nhưng có trong list 2 là: ",different_1)
    for i in C19_2:
        if i not in C19_1:
            different_2.append(i)
    print("Các phần tử có trong list 2 nhưng có trong list 1 là: ", different_2)
def ex21():
    C21 = ["D","A","N","H"]
    print("Chuỗi sau tạo là: ","".join(C21))
# 24. Write a Python program to append a list to the second list.
def ex24():
    C24_1 = [1,2,3,4,5,6,7]
    C24_2 = [8,9,10,11,12,13,14]
    C24_1.extend(C24_2)
    print("Chuỗi mới sau khi nối 2 chuỗi lại với nhau là: ",C24_1)
#Câu 25 Write a Python program to select an item randomly from a list.
def ex25():
    C25 = [1,2,3,4,5,6,7,8,9]
    Chon_ra = random.choice(C25)
    print("Số được chọn ra ngẫu nhiên từ chuỗi là: ",Chon_ra)
#Câu 27: Write a Python program to find the second smallest number in a list.
def ex27():
    C27 = [1,2,3,4,5,6,7,8,9,10]
    C27_smallest = C27[1]
    for i in C27:
        if i < C27_smallest:
            C27_smallest = i
    print("Số nhỏ thứ hai trong chuỗi là: ",C27_smallest)
#Câu 29. Write a Python program to get unique values from a list.
def ex29():
    C29 = [1,2,3,4,2,2,2,1,5,3,4,3932,383]
    unique = []
    for i in C29:
        if i not in unique:
            unique.append(i)
    print("Chuỗi sau khi chỉ hiện giá trị duy nhất là: ",unique)
# 36. Write a Python program to get a variable with an identification number or string
def ex36():
    C36_1 = float(input("Hãy nhập một biến kiểu số: "))
    C36_2 = input("Hãy nhập một biến kiểu chuỗi: ")
    print("Số nhận dạng của biến kiểu số là: ",id(C36_1))
    print("Số nhận dạng của biến kiểu chuỗi là: ",id(C36_2))
    print("Chuỗi biểu diễn của biến kiểu số là: ",str(C36_1))
    print("Chuỗi biểu diễn của biến kiểu chuỗi là: ",str(C36_2))
# 37. Write a Python program to find common items in two lists.
def ex37():
    C37_1 = [1,2,3,4,5,6,7,8,9,10]
    C37_2 = [1,3,5,7,9,15,17,19,21,23,25,27,29,101]
    giong_nhau = []
    for i in C37_1:
        if i in C37_2:
            giong_nhau.append(i)
    print("Những phần tử giống nhau giữa hai danh sách là: ",giong_nhau)


ex37()