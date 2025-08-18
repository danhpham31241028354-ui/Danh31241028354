#Câu 1: Write a Python program to calculate the length of a string.
chuoi = str(input("(Câu 1) Hãy nhập một chuỗi nào đó: "))
print(len(chuoi))
#Câu 2: Write a Python program to count the number of characters (character frequency) in a string
c = str(input(" (Câu 2) Hãy nhập chuỗi: "))
c_count = {} #Tạo dictionary rỗng để lưu kết quả
for char in c:
    if char not in c_count:
        c_count[char] = 1 #Nếu chưa có thì thêm vào là 1
    else:
        c_count[char] += 1 #Đã có rồi --> cộng thêm 1
print("Kết quả thu được",c_count)
#Câu 3: Write a Python program to get a string made of the first 2 and last 2 characters of a given
# string. If the string length is less than 2, return the empty string instead.
d = str(input("(Câu 3) Hãy nhập chuỗi: "))
if len(d) < 2:
    ket_qua = ""
else:
    ket_qua = d[:2] + d[-2:] #Lấy 2 ký tự đầu và 2 ký tự cuối nếu chuỗi > 2
print("Kết quả thu được: ",ket_qua)
#Câu 11: Write a Python program to remove characters that have odd index values in a given string
e = str(input("(Câu 11) Hãy nhập chuỗi: "))
kq = e[::2] #Bước nhảy là 2 --> lấy các số chẵn
print(kq)
# Câu 12: Write a Python program to count the occurrences of each word in a given sentence.
f = str(input("(Câu 12) Hãy nhập chuỗi: "))
f_count = {}
for char in f:
    if char not in f_count:
        f_count[char] = 1
    else:
        f_count[char] += 1
print("Kết quả thu được: ",f_count)
#Câu 13: Write a Python script that takes input from the user and displays that input back in upper
# and lower cases.
g = str(input("(Câu 13) Hãy nhập chuỗi: "))
print(g.upper())
print(g.lower())
#Câu 14: Write a Python program that accepts a comma-separated sequence of words as input and
#prints the distinct words in sorted form (alphanumerically).
h = str(input("(Câu 14) Hãy nhập các từ cách nhau bằng dấu phẩy: ")).split(",")
loai_bo_tu_lap = set(h) #Loại bỏ các từ trùng lặp --> còn các từ khác nhau
tu_duoc_sap_xep = sorted(loai_bo_tu_lap) #Dùng sorted để sắp xếp theo bảng chữ cái
print(",".join(tu_duoc_sap_xep)) #Join: Nối các từ lại. Ví dụ "apple, banana, orange"
#Câu 18: Write a Python function to get a string made of the first three characters of a specified string.
# If the length of the string is less than 3, return the original string.
j = str(input("(Câu 18) Hãy nhập chuỗi: "))
if len(j) < 3:
    Ket_qua = j
else:
    Ket_qua = j[:3]
print("Kết quả thu được: ",Ket_qua)
#Câu 20: Write a Python function to reverse a string if its length is a multiple of 4.
k = str(input("(Câu 20) Hãy nhập chuỗi: "))
if len(k) % 4 == 0:
    KQ = k[::-1] #Đảo ngược chuỗi
else:
    KQ = k
print("Kết quả thu được: ",KQ)
#Câu 22: Write a Python program to sort a string lexicographically (Thứ tự từ điển --> Như thứ tự bảng chữ cái)
l = str(input("(Câu 22) Hãy nhập chuỗi: "))
sap_xep = sorted(l)
print("".join(sap_xep))
#Câu 23: Write a Python program to remove a newline in Python.
m = "Hello\nWorld"
print("(Câu 23) Chuỗi sau khi xóa dòng mới là: ",m.replace("\n",""))
#Câu 30: Write a Python program to print the following numbers up to 2 decimal places.
n = float(input("(Câu 30) Nhập một số bất kỳ: "))
print("Số đó được in ra với 2 chữ số thập phân là {:.2f}".format(n))
#Câu 31: Write a Python program to print the following numbers up to 2 decimal places with a sign.
o = float(input("(Câu 31) Nhập một số bất kỳ: "))
print("Số đó được in ra với 2 chữ số thập phân là {:+.2f}".format(o)) #{:+.2f}: làm tròn 2 chữ số sau dấu phẩy. Đồng thời thêm (+) nếu là số dương và (-) nếu là số âm
#Câu 32: Write a Python program to print the following positive and negative numbers with no
#decimal places.
p = float(input("(Câu 32) Nhập một số bất kỳ: "))
print("Số đó được in ra với 2 chữ số thập phân là {:+.0f}".format(o))
#Câu 35: Write a Python program to display a number with a comma separator.
q = float(input("(Câu 35) Nhập một số bất kỳ: "))
print("Số in ra được phân cách bởi dấu phẩy: ",format(q,",")) #format(q,",") là ngăn cách số q được nhập bởi các dấu phấy: Ví dụ 378723 = 378,723

#Câu 36: Write a Python program to format a number with a percentage.
r = float(input("(Câu 36) Nhập một số bất kỳ: "))
print("Số đó được viết dưới dạng phần trăm là: {:.0%}".format(r))
#Câu 37: Write a Python program to display a number in left, right, and center aligned with a width of 10.
t = float(input("(Câu 37) Nhập một số bất kỳ: "))
#Căn trái là <; 10 là độ rộng, căn phải >, căn giữa ^
print("Căn trái: {:<10}".format(t))
print("Căn phải: {:>10}".format(t))
print("Căn giữa: {:^10}".format(t))
#Câu 39: Write a Python program to reverse a string.
u = str(input("(Câu 39) Hãy nhập một chuỗi: "))
print(f"Chuỗi {u} sau khi đảo là: ",u[::-1])
#Câu 40: Write a Python program to reverse words in a string.
#Hướng giải: Nhập chuỗi --> Tách từ --> Đảo từ --> Nối từ thành chuỗi --> In ra
v = str(input("(Câu 40) Hãy nhập một chuỗi: "))
tach_tu_trong_v = v.split() #Tách từ trong chuỗi mới nhập ra
dao_tu = tach_tu_trong_v[::-1] #Đảo ngược từ từ mấy từ đó
noi_thanh_chuoi_moi = " ".join(dao_tu) #Nối các từ sau khi đảo thành chuỗi mới
print(f"Chuỗi {v} sau khi đảo các từ là: ",noi_thanh_chuoi_moi) #In ra sau khi nối
#Câu 41: Write a Python program to strip a set of characters from a string.
w = str(input("(Câu 41): Hãy nhập một chuỗi: "))
w1 = str(input("Hãy nhập ký tự muốn bỏ: "))
#Code bỏ ký tự
for char in w1:
    w = w.replace(char,"")
print(f"Chuỗi {w} sau khi đã loại bỏ ký tự là: ",w)
#Câu 42: Write a Python program to count repeated characters in a string.
x = str(input("(Câu 42) Hãy nhập một chuỗi: "))
counts = {}
#Đếm ký tự trong chuỗi
for char in x:
    if char in counts:
        counts[char] +=1
    else:
        counts[char] = 1
#In ra các ký tự lặp lại
for char in counts:
    if counts[char] > 1:
        print(char,counts[char])
#Câu 43: Write a Python program to print the square and cube symbols in the area of a rectangle and
# the volume of a cylinder.
# Sample output:
# The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3
import math
chieu_dai = float(input("(Câu 43) Hãy nhập chiều dài hình chữ nhật (cm): "))
chieu_rong = float(input("(Câu 43) Hãy nhập chiều rộng hình chữ nhật (cm): "))
ban_kinh = float(input("(Câu 43) Hãy nhập bán kính hình trụ (cm): "))
chieu_cao = float(input("(Câu 43) Hãy nhập chiều cao hình trụ (cm): "))
dien_tich_hinh_chu_nhat = chieu_dai*chieu_rong
the_tich_hinh_tru = math.pi*chieu_cao*pow(ban_kinh,2)
print(f"Diện tích hình chữ nhật là {dien_tich_hinh_chu_nhat:.2f} cm2")
print(f"Thể tích hình trụ là {the_tich_hinh_tru:.3f} cm3")
#Câu 46: Write a Python program to convert a given string into a list of words.
z = str(input("(Câu 46) Hãy nhập một chuỗi: "))
print("Danh sách các từ là:  ",z.split())
#Câu 47: Write a Python program to lowercase the first n characters in a string.
A = str(input("(Câu 47) Hãy nhập một chuỗi: "))
n1 = int(input("(Câu 47) Hãy nhập số ký tự bạn muốn chuyển thành chữ thường: "))
A1 = A[:n1].lower() + A[n1:]
print("Kết quả thu được là: ",A1)
#Câu 49: Write a Python program to count and display vowels in text.
B = str(input("(Câu 49) Hãy nhập một chuỗi: "))
nguyen_am = "ueoaiUEOAI" #Liệt kê các nguyên âm ra
count = 0 #Đếm, ban đầu bằng 0
print(f"Các nguyên âm có trong chuỗi {B}là: ")
for char in B:
    if char in nguyen_am:
        print(char,end=" ")
        count +=1 #Mỗi lần tìm ra được nguyên âm thì cộng thêm 1 vào biến count
print("\nTổng số nguyên âm là: ",count)
#Câu 50: Write a Python program to split a string on the last occurrence of the delimiter
C = str(input("(Câu 50) Hãy nhập một chuỗi: "))
delimiter = str(input("Nhập ký tự cần phân tách: "))
tach = C.rsplit(delimiter,1) #Dùng rsplit với maxsplit = 1 để chỉ tách 1 lần từ bên phải
print("Kết quả thu được là: ",tach)
#Câu 55: Write a Python program to find the first repeated word in a given string
D = str(input("(Câu 55) Hãy nhập một chuỗi: "))
words = D.split() #Tách các từ trong chuỗi vừa nhập ra
for w in words:
    if words.count(w) > 1: #Nếu từ đó xuất hiện nhiều hơn 1 lần
        print("Từ lặp đầu tiên là: ",w)
        break
#Câu 57: Write a Python program to remove spaces from a given string
E = str(input("(Câu 57) Hãy nhập một chuỗi: "))
print(f"Chuỗi {E} sau khi bỏ khoảng trống là: ",E.replace(" ",""))
#Câu 58: Write a Python program to move spaces to the front of a given string.
F = str(input("(Câu 58) Hãy nhập một chuỗi: "))
space = F.count(" ") #Đếm số khoảng trắng
KQua = " "*space + F.replace(" ","") #" "*space --> Đưa hết khoảng trắng ra đầu; F.replace: Phần còn lại trong chuỗi + bỏ hết khoảng trắng
print("Kết quả thu được là: ",KQua)
# Câu 59: Write a Python program to find the maximum number of characters in a given string.
G  = str(input("(Câu 59) Hãy nhập một chuỗi: "))
max_char = "" #Ký tự xuất hiện nhiều nhất
max_count = 0 #Số lần xuất hiện nhiều nhất
for char in G:
    count = G.count(char) #Đếm số lần ký tự c xuất hiện trong chuỗi
    if count > max_count:
        max_count = count
        max_char = c
print("Ký tự xuất hiện nhiều nhất là: ",max_char)
print("Số lần xuất hiện: ",max_count)
#Câu 61: Write a Python program to remove duplicate characters from a given string.
H = str(input("(Câu 61) Hãy nhập một chuỗi: "))
result = "" #Tạo một chuỗi rỗng để lưu kết quả
for char in H:
    if char not in result:
        result += char #Nếu ký tự chưa có trong result thì thêm ký tự vào result
print(f"Chuỗi {H} sau khi bỏ ký tự trùng: ",result)
#Câu 62: Write a Python program to compute the sum of the digits in a given string.
I = str(input("(Câu 62) Hãy nhập một chuỗi: "))
tong = 0 #Biến để lưu tổng các chữ số
for char in I:
    if char.isdigit(): #Nếu ký tự đó là số
        tong+= int(char)
print(f"Tổng các chữ số trong chuỗi {I} là: ",tong)
#Câu 71: Write a Python program to move all spaces to the front of a given string in a single traversal.
J = str(input("(Câu 71) Hãy nhập một chuỗi: "))
space = "" #Để chứa các khoảng trắng
chars = "" #Để chứa các ký tự khoảng trắng
for char in J:
    if char == " ": #Nếu là khoảng trắng
        space += char #Thêm vào biến space
    else:
        chars += char #Nếu không, thêm vào biến chars
#Ghép khoảng trắng lên trước rồi đến phần còn lại
KQUA = space + chars
print(f"Chuỗi {J} sau khi chuyển: ",KQUA)
#Câu 72: Write a Python program to remove all characters except a specified character from a given
# string.
K = str(input("(Câu 72) Hãy nhập một chuỗi: "))
ch = str(input("Nhập ký tự cần giữ lại: "))
#Giữ lại các ký tự trùng với ch
RESULT = ""
for char in K:
    if char == ch:
        RESULT += char
print("Kết quả thu được là: ",RESULT)
#Câu 73: Write a Python program to count Uppercase, Lowercase, special characters and numeric
# values in a given string.
L = str(input("(Câu 73) Hãy nhập một chuỗi: "))
uppercase = 0
lowercase = 0
digits = 0
special = 0
for char in L:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        digits += 1
    else:
        special += 1
print("Chữ hoa: ",uppercase)
print("Chữ thường: ",lowercase)
print("Chữ số: ",digits)
print("Ký tự đặc biệt: ",special)
#Câu 77: Write a Python program to count the number of non-empty substrings of a given string.
M = str(input("(Câu 77) Hãy nhập một chuỗi: "))
M2 = len(M)
#Công thức tính số chuỗi con (substring) không rỗng
M3 = M2*(n+1)//2 #Sử dụng // do chia lấy phần nguyên
print(f"Số lượng chuỗi con không rỗng của chuỗi {M} là:  ",M3)
#Câu 79: Write a Python program to find the smallest and largest words in a given string.
N = str(input("(Câu 79) Hãy nhập một chuỗi: "))
N1 = N.split() #Tách chuỗi thành các từ
#Giả sử ban đầu từ đầu tiên là ngắn nhất và dài nhất
smallest = N1[0]
largest = N1[0]
for word in N1:
    if len(word) < len(smallest):
        smallest = word
    if len(word) > len(largest):
        largest = word
print("Từ ngắn nhất: ",smallest)
print("Từ dài nhất: ",largest)
#Câu 80: Write a Python program to count the number of substrings with the same first and last characters in a given string.
O = str(input("(Câu 80) Hãy nhập một chuỗi: "))
COUNT = 0
O1 = len(O)
for i in range(O1):
    for j in range(i,O1):
        if O[i] == O[j]:
            COUNT += 1
print("Số lượng chuỗi con có ký tự đầu và cuối giống nhau là: ",COUNT)
#Câu 84: Write a Python program to swap cases in a given string
P = str(input("(Câu 84) Hãy nhập một chuỗi: "))
KQL = P.swapcase() #Hoán đổi chữ hoa và chữ thường
print(f"Chuỗi {P} sau khi hoán đổi là: ",KQL)
#Câu 86: Write a Python program to delete all occurrences of a specified character in a given string
Q = str(input("(Câu 86) Hãy nhập một chuỗi: "))
Q1 = str(input("Hãy nhập ký tự muốn xóa: "))
KQR = ""
for char in Q:
    if char != Q1: #Nếu ký tự khác với ký tự cần xóa thì giữ lại
        KQR += char
print("Chuỗi sau khi xóa là: ",KQR)
#Câu 87: Write a Python program to find the common values that appear in two given strings
R1 = str(input("(Câu 87) Hãy nhập chuỗi thứ nhất: "))
R2 = str(input("(Câu 87) Hãy nhập chuỗi thứ hai: "))
COMMON = ""
for char in R1:
    if (char in R2) and (char not in COMMON):
        COMMON += char
print(f"Các ký tự chung của chuỗi {R1} và chuỗi {R2} là: ",COMMON)
#Câu 88: Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length.
S = str(input("(Câu 88) Hãy nhập một chuỗi: "))
has_upper = False
has_lower = False
has_digit = False
min_lenght = 8 #Đặt độ dài tối tiếu của chuỗi
for char in S:
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    if char.isdigit():
        has_digit = True
if has_upper and has_lower and has_digit and len(s) >= min_lenght:
    print("Chuỗi hợp lệ: có in hoa, thường, số và đủ độ dài.")
else:
    print("Chuỗi không hợp lệ.")
#Câu 89: Write a Python program to remove unwanted characters from a given string.
T = str(input("(Câu 89) Hãy nhập một chuỗi: "))
unwanted = str(input("Hãy nhập ký tự không muốn: "))
RS = "".join(char for char in T if char not in unwanted)
print(f"Chuỗi {T} sau khi loại bỏ {unwanted} là: ",RS)
#Câu 90: Write a Python program to remove duplicate words from a given string.
U = str(input("(Câu 90) Hãy nhập chuỗi: "))
U1 = U.split()
RST = " ".join(dict.fromkeys(U1)) #Loại bỏ từ trùng lặp nhưng vẫn giữ thứ tự ban đầu
print(f"Chuỗi {U} sau khi loại bỏ thứ tự trùng lặp là: ",RST)
#Câu 93: Write a Python program to extract numbers from a given string.
V = str(input("(Câu 93) Hãy nhập một chuỗi: "))
V1 = [] #Tạo danh sách rỗng để chứa các số
for word in V.split():
    if word.isdigit(): #Nếu từ là số
        V1.append(int(word)) #Chuyển về int và thêm vào danh sách --> append
print(f"Các số trong chuỗi {V} là: ",V1)
#Câu 96: Write a Python program to convert a given string to Camelcase.
Y = str(input("(Câu 96) Hãy nhập một chuỗi: "))
Y1 = Y.split()
camel = ""
for word in Y1:
    camel += word.capitalize() #Viết hoa chữ cái đầu của từng chữ
print("Chuỗi dạng CamelCase: ",camel)
#Câu 97: Write a Python program to convert a given string to Snake case.
Z = str(input("(Câu 97) Hãy nhập một chuỗi: "))
snake = Z.lower().replace(" ","_") #Nối các từ thành dấu gạch dưới và chuyển thành chữ thường
print("Chuỗi dạng Snake Case: ",snake)
#Câu 98: Write a Python program to decapitalize the first letter of a given string.
C98 = str(input("(Câu 98) Hãy nhập một chuỗi: "))
if C98: #Kiểm tra chuỗi không rỗng
    RSL = C98[0].lower() + C98[1:] #Chuyển ký tự đầu thành chữ thường,giữ nguyên các ký tự sau
    print(f"Chuỗi {C98} sau khi chuyển là: ",RSL)
else:
    print("Chuỗi rỗng")
#Câu 99: Write a Python program to split a multi-line string into a list of lines.
C99 = str(input("(Câu 99) Nhập các dòng, cách nhau bằng dấu |:"))
lines = C99.split("|") #Tách chuỗi thành danh sách các dòng
print(lines)
#Câu 10: Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
C10 = str(input("(Câu 10) Hãy nhập một chuỗi: "))
chuoi_moi = C10[-1] + C10[1:-1]  + C10[0]
print(f"Chuỗi {C10} sau khi hoán đổi ký tự đầu và cuối là: ",chuoi_moi)









