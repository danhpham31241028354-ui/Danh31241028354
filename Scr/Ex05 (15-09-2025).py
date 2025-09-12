# Set
# 1.Write a Python program to find the maximum and minimum values in a set.
def C1():
    C1 = {2023,2024,2025,2026,2027,2028,2029,2030}
    print("Số lớn nhất là: ",max(C1))
    print("Số nhỏ nhất là: ",min(C1))
# 2.Write a Python program to check if a given value is present in a set or not.
def C2():
    C2 = {1,2,3,4,5,6,7,8,9,10}
    n = int(input("Nhập một số bất kỳ mà bạn muốn kiểm tra: "))
    if n in C2:
        print(f"Số {n} có trong tập hợp")
    else:
        print(f"Số {n} không có trong tập hợp")
# 3.Write a Python program to check if two given sets have no elements in common.
def C3():
    C3_1 = {1, 10, 11, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030,2031}
    C3_2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11}
    C3_chung = set()
    for x in C3_1:
        if x in C3_2:
            C3_chung.add(x)
    if C3_chung:
        print("Hai tập hợp có phần tử chung. Các phần tử chung đó là: ",C3_chung)
    else:
        print("Hai tập hợp không có phần tử chung")
# 4.Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
def C4():
    C4 = ["apple","banana","cherry","apple"]
    C4_set = set(C4)
    print("Các từ chỉ xuất hiện một lần là: ",C4_set)
    for word in C4:
        print(f"{word}:{C4.count(word)}")
# 5.Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.
def C5():
    C5_1 = {1, 10, 11, 12, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030,2031}
    C5_2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    C5_chung_1 = set()
    C5_chung_2 = set()
    for x in C5_1:
        if x not in C5_2:
            C5_chung_1.add(x)
    print("Các số có trong set 1 mà không có trong set 2 là: ",C5_chung_1)
    for x in C5_2:
        if x not in C5_1:
            C5_chung_2.add(x)
    print("Các số có trong set 2 mà không có trong set 1 là: ",C5_chung_2)
C5()
#Dictionary
# Dictionary ban đầu: mỗi nhân viên có ID, tên, phòng ban, lương
employees = {
    101: {"name": "Alice", "department": "HR", "salary": 5000},
    102: {"name": "Bob", "department": "IT", "salary": 6000},
    103: {"name": "Charlie", "department": "Finance", "salary": 5500},
    104: {"name": "David", "department": "IT", "salary": 6500},
    105: {"name": "Eva", "department": "HR", "salary": 5200}
}
#Tạo dictionary mới để nhóm nhân viên theo phòng ban"
dept_employees = {}
for emp_id, info in employees.items():
    dept = info["department"]   # Lấy phòng ban của nhân viên
    name = info["name"]
    salary = info["salary"]
    # Nếu phòng ban chưa tồn tại trong dept_employees thì thêm vào
    if dept not in dept_employees:
        dept_employees[dept] = {}
    # Thêm nhân viên vào phòng ban tương ứng
    dept_employees[dept][name] = salary
# In kết quả
print("Dictionary gốc (employees):")
print(employees)
print("\nDictionary nhóm theo phòng ban (dept_employees):")
print(dept_employees)