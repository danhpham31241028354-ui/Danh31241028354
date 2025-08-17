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








