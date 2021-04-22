a1 = input("请输入数字：")
a2 = input("请输入数字：")
a3 = input("请输入数字：")
a4 = input("请输入数字：")
a5 = input("请输入数字：")
a6 = input("请输入数字：")
a7 = input("请输入数字：")
a8 = input("请输入数字：")
a9 = input("请输入数字：")
a10 = input("请输入数字：")

total = int(a1)+int(a2)+int(a3)+int(a4)+int(a5)+int(a6)+int(a7)+int(a8)+int(a9)+int(a10)
print("和:",total)

print("最大值:",max(int(a1),int(a2),int(a3),int(a4),int(a5),int(a6),int(a7),int(a8),int(a9),int(a10)))

print("平均数:",total/10)

import random
num = random.randint(50,150)
print(num)

a = int(input("请输入数值:"))
b = int(input("请输入数值:"))
c = int(input("请输入数值:"))
if a+b<=c or a+c<=b or b+c<=a:
    print("不能构成三角形")
elif a^2 + b^2 == c^2 or a^2 + c^2 == b^2 or b^2 + c^2 == a^2 :
    print("直角三角形")
elif a == b and a != c or b == c and a != c or a == c and b != c:
    print("等腰三角形")
elif a == b == c :
    print("等边三角形")
else:
    print("普通三角形")

A = (int(input("请输入数值A:")))
B = (int(input("请输入数值B:")))
C = (A + B)
A = (C - A)
B = (C - B)
print("A的数值",A)
print("B的数值",B)


name = "root"
password = "admin"
count = 0
while count <= 3:
    count = count + 1
    name1 = input("请输入用户名:")
    password1 = input("请输入密码:")
    if name1 == name and password == password1:
        print("登录成功")
    elif name1 == name and count == 4 and password != password1:
        print("密码冻结")
    elif name1 == name and password != password1:
        print("密码错误")
    else:
        print("登录失败")
        break
