import random
# 1. Write a Python program to sum all the items in a list.
import random
lst = []
for i in range(1,20):
    lst.append(random.randint(1,50))
def print_list():
    print(lst)
def ex_01():
    sum = 0
    for item in lst:
        sum+= item
    print(f"Sum of all characters in a list is {sum} ")
# 2. Write a Python program to multiply all the items in a list.
def ex_02():
    multiply = 1
    for item in lst:
        multiply *= item
    print(f"The multiplication of all characters in a list is {multiply}")
# 3. Write a Python program to get the largest number from a list.
def ex_03():
    largest = lst[0]
    for item in lst:
        if item > largest:
            largest = item
    print(f"The largest number of the list is {largest}")
# 4. Write a Python program to get the smallest number from a list.
def ex_04():
    smallest = lst[0]
    for item in lst:
        if item < smallest:
            smallest = item
    print(f"The smallest number of the list is {smallest}")
# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
def ex_05():
    str = ["saghsahsa","hsahsah","shsbsbhs"]
    dem = 0
    for st in str:
        if len(st) < 2:
            continue
    if st[0] == st[-1*len(st)]:
        dem+=1
    print(f"Result: {dem}")
#7. Write a Python program to remove duplicates from a list.
def ex_07():
    for item in lst:
        while lst.count(item) > 1: #Lọc toàn bộ chuỗi --> Dùng if chỉ loại được 1 phần tử lặp, còn các phần từ khác nếu có duplicates thì vẫn lặp
            lst.remove(item)
    print(f"The list after removing duplicates is: {lst} ")
# 8.Write a Python program to check if a list is empty or not.
def ex_08():
    if len(lst) == 0:
        print("The list is empty")
    else:
        print("The list isn't empty")
# 9.Write a Python program to clone (nhân bản) or copy a list
def ex_09():
    lst_duoc_copy = lst.copy()
    print(f"List after being copied is {lst_duoc_copy}")
    lst_duoc_nhan_ban = lst*2
    print(f"List after being cloned is {lst_duoc_nhan_ban}")
# 10. Write a Python program to find the list of words that are longer than n from a
# given list of words.
def ex_10():
    chuoi_tu_nhap = ["pham","thanh","danh","ptd","hr"]
    n = int(input("Please type the number of characters you want to overcome: "))
    chuoi_moi_sau_kiem_tra = []
    for st in chuoi_tu_nhap:
        if len(st) > n:
            chuoi_moi_sau_kiem_tra.append(st)
    print(f"List of words that are longer than {n} from {chuoi_tu_nhap} is {chuoi_moi_sau_kiem_tra}")
# 12. Write a Python program to print a specified list after removing the 0th, 4th
# and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
def ex_12():
    chuoi_nhap =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    chuoi_nhap_moi = chuoi_nhap[1:4]
    print(chuoi_nhap_moi)
print_list()
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
# 65. Write a Python program to move all zero digits to the end of a given list of
# numbers.
# Expected output:
# Original list:
# [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# Move all zero digits to end of the said list of numbers:
# [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ex65():
    C65 = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
    C65_ket_qua = [x for x in C65 if x != 0] + [0]*C65.count(0) #+ [0]: in ra thêm danh sách có số 0, *count(0): có bao nhiêu số 0 ở danh sách cũ thì danh sách mới có bấy nhiêu số 0
    print("Kết quả là: ", C65_ket_qua)
# 66. Write a Python program to find the list in a list of lists whose sum of elements
# is the highest.
# Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# Expected Output: [10, 11, 12]
def ex66():
    C66 = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
    C66_ket_qua = max(C66, key = sum) #max(iterable, key = function) + iterable: danh sách; key: hàm dùng để so sánh kết quả
    print("Danh sách có kết quả lớn nhất là: ",C66_ket_qua)
# 67. Write a Python program to find all the values in a list that are greater than a specified number.
def ex67():
    C67 = [1,2,3,4,5,6,7,8,9,10]
    C67_num = 3
    C67_moi = []
    for i in C67:
        if i > C67_num:
            C67_moi.append(i)
    print("Tất cả các phần tử trong danh sách lớn hơn số đã cho là: ",C67_moi)
# 68. Write a Python program to extend a list without appending.
# Sample data: [10, 20, 30]
# [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]
def ex68():
    C68_1 = [10, 20, 30]
    C68_2 = [40, 50, 60]
    C68_1.extend(C68_2)
    print("Danh sách mới là: ",C68_1)
# 73. Write a Python program to remove consecutive (following each other
# continuously) duplicates (elements) from a given list.
# Original list:[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After removing consecutive duplicates:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
def ex73():
    C73 = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    C73_ket_qua = []
    for item in C73:
        if not C73_ket_qua or item != C73_ket_qua[-1]:
            C73_ket_qua.append(item)
    print(C73_ket_qua)
# 74. Write a Python program to pack consecutive duplicates of a given list of
# elements into sublists.
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After packing consecutive duplicates of the said list elements into sublists:
# [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
def ex74():
    C74 = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    C74_ket_qua = []
    for item in C74:
        if not C74_ket_qua or item != C74_ket_qua[-1][-1]:
            C74_ket_qua.append([item])
    print(C74_ket_qua)
# 78. Write a Python program to split a given list into two parts where the length of
# the first part of the list is given.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# Length of the first part of the list: 3
# Splited the said list into two parts:
# ([1, 1, 2], [3, 4, 4, 5, 1])
def ex78():
    C78 = [1, 1, 2, 3, 4, 4, 5, 1]
    n = 3
    C78_1 = C78[:n]
    C78_2 = C78[n:]
    print("Danh sách thứ nhất sau khi tách: ",C78_1)
    print("Danh sách thứ hai sau khi tách: ",C78_2)
# 79. Write a Python program to remove the K'th element from a given list, and
# print the updated list.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# After removing an element at the kth position of the said list:
# [1, 1, 3, 4, 4, 5, 1]
def ex79():
    C79 = [1, 1, 2, 3, 4, 4, 5, 1]
    del C79[2]
    print("Danh sách mới sau khi xóa phần tử thứ hai là: ",C79)
# 80. Write a Python program to insert an element at a specified position into a
# given list.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# After inserting an element at kth position in the said list:
# [1, 1, 12, 2, 3, 4, 4, 5, 1]
def ex80():
    C80 = [1, 1, 2, 3, 4, 4, 5, 1]
    C80.insert(2,12)
    print("Danh sách sau khi chèn thêm phần tử vào vị trí thứ 2 là: ",C80)
# 81. Write a Python program to extract a given number of randomly selected
# elements from a given list.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# Selected 3 random numbers of the above list: --> Dùng random.sample
# [4, 4, 1]
def ex81():
    C81 = [1, 1, 2, 3, 4, 4, 5, 1]
    C81_chon = random.sample(C81,3)
    print(f"3 phần tử được chọn từ danh sách là {C81_chon}")
# 102. Write a Python program to extract specified size of strings from a give list of
# string values.
# Original list:
# [' Python', 'list', 'exercises', 'practice', 'solution']
# length of the string to extract:
# 8
# After extracting strings of specified length from the said list:
# ['practice', 'solution']
def ex102():
    C102 = ['Python', 'list', 'exercises', 'practice', 'solution']
    length_to_extract = 8
    C102_result = [s.strip() for s in C102 if len(s.strip()) == length_to_extract]
    print(C102_result)

ex102()