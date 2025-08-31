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
# 39. Write a Python program to convert a list of multiple integers into a single
# integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350
def ex39():
    C39 = [11,33,50]
    print("Số sau khi chuyển từ danh sách là: ",int("".join(str(x) for x in C39)))
# 41. Write a Python program to create multiple lists.
def ex41():
    C41_1 = [1,2,3,4]
    C41_2 = [5,6,7,8,9,10]
    C41_3 = ["True", "False", "Not Given"]
    print("Danh sách 1: ",C41_1)
    print("Danh sách 2: ",C41_2)
    print("Danh sách 3: ",C41_3)
# 42. Write a Python program to find missing (có trong list 1 nhưng không có trong list 2) and additional values (có trong list 2 nhưng không có trong list 1) in two lists.
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h
def ex42():
    C42_1 = ["a","b","c","d"]
    C42_2 = ["a","g","h"]
    co_1_khong_2 = []
    co_2_khong_1 = []
    for st in C42_1:
        if st not in C42_2:
            co_1_khong_2.append(st)
    print("Ký tự bị thiếu trong danh sách 1 là: ",co_1_khong_2)
    for st in C42_2:
        if st not in C42_1:
            co_2_khong_1.append(st)
    print("Ký tự được thêm vào là: ",co_2_khong_1)
# 43. Write a Python program to split a list into different variables.
def ex43():
    C43 = ["Phạm","Thành","Danh"]
    print("Chữ đầu tiên của danh sách là: ",C43[0])
    print("Chữ thứ hai của danh sách là: ",C43[1])
    print("Chữ thứ ba của danh sách là: ",C43[2])
# 44. Write a Python program to generate groups of five consecutive numbers in a ist.
def ex44():
    C44_number = list(range(1,16))
    C44_group = []
    for i in range(0,len(C44_number),5):#Quét hết các phần tử từ thứ 0 đến phần tử cuối của danh sách (len(C44_number)) với bước nhảy là 5: 5 số 1 nhóm
        C44_group_nho = C44_number[i:i+5]
        C44_group.append(C44_group_nho)
    print("Danh sách mới sau khi nhóm là: ",C44_group)
# 46. Write a Python program to select the odd items from a list.
def ex46():
    C46 = [1,2,3,4,5,6,7,8,9,10]
    C46_le = []
    for i in C46:
        if i % 2 != 0:
            C46_le.append(i)
    print("Danh sách các phần tử lẻ là: ",C46_le)
# 47. Write a Python program to insert an element before each element of a list.
def ex47():
    C47 = [1,2,3,4,5]
    element = 0
    C47_new_list = []
    for i in C46:
        C47_new_list.append(element)
        C47_new_list.append(i)
    print("Danh sách mới là: ",C47_new_list)
# 48. Write a Python program to print nested lists (each list on a new line) using the print() function.
def ex48():
    C48 = [[1,2,3],[4,5,6,7,8],[9,10]]
    for sublist in C48:
        print(sublist)
# 51. Write a Python program to split a list every Nth element
def ex51():
    C51 = ["P","H","A","M","T","H","A","N","H","D","A","N","H"]
    C51_group = []
    for st in range (0,len(C51),5):
        C51_group_nho = C51[st:st+5]
        C51_group.append(C51_group_nho)
    print("Danh sách mới sau khi nhóm là: ",C51_group)
# 52. Write a Python program to compute the difference between two lists.
def ex52():
    C52_1 = ["red", "orange", "green", "blue", "white"]
    C52_2 =  ["black", "yellow", "green", "blue"]
    khac_1 = []
    khac_2 = []
    for st in C52_1:
        if st not in C52_2:
            khac_1.append(st)
    print("Color 1 - Color 2: ",khac_1)
# 53. Write a Python program to create a list with infinite elements.
def infinite_list():
    num = 1
    while True:
        yield num
        num += 1
gen = infinite_list()
for i in range(20):
    print(next(gen))
# 54. Write a Python program to concatenate elements of a li
def ex54():
    C54 = ["Pham","Thanh","Danh"]
    print("Danh sách mới sau khi nối là: ","".join(C54))
# 56. Write a Python program to convert a string to a list
def ex56():
    C56 = "Harrypham"
    C56_tach = list(C56)
    print(f"Chuỗi {C56} sau khi tách thành danh sách là: {C56_tach} ")
# 57. Write a Python program to check if all items in a given list of strings are equal to a given string.
def ex57():
    fruits = ["apple","apple","apple"]
    check = "cherry"
    Dung = True
    for item in fruits:
        if item != check:
            Dung = False
    if Dung:
        print("Danh sách đã cho đúng với chuỗi cần check")
    else:
        print("Danh sách đã cho khác với chuỗi cần check")
# 58. Write a Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
def ex58():
    C58_1, C58_2 = [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
    C58_1_moi = C58_1[:-1]
    C58_1_moi.extend(C58_2)
    print("Danh sách sau khi gộp vào là: ",C58_1_moi)
def ex59():
    C59 = [1,2,3,4,5]
    C59_n = int(input("Hãy nhập vị trí bạn muốn kiểm tra: "))
    if C59_n >= 0 and C59_n < len(C59):
        print("Phần tử đó tồn tại trong danh sách")
    else:
        print("Phần tử đó không tồn tại trong danh sách")
# 62. Write a Python program to print a list of space-separated elements.
def ex62():
    C62 = [1,2,3,4,"Thanh","Danh"]
    print("Các phần tử của danh sách cách nhau bởi khoảng trống là: "," ".join(str(x) for x in C62))
# 63. Write a Python program to insert a given string at the beginning of all items in a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
def ex63():
    C63 = [1,2,3,4]
    C63_str = input("Hãy nhập một chuỗi: ")
    C63_moi = []
    for i in C63:
        C63_moi.append(C63_str + str(i))
    print("Danh sách sau khi nối với chuỗi được nhập là: ",C63_moi)
# 64. Write a Python program to iterate over two lists simultaneously. --> Dùng zip() để lặp đồng thời hai danh sách
def ex64():
    C64_1 = [1,2,3,4]
    C64_2 = ["a","b","c","d"]
    for x, y in zip(C64_1,C64_2):
        print(x,y)

ex64()

