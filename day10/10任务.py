#一
import pymysql

con = pymysql.connect(host="localhost",user="root",password="",database="day10")
cursor = con.cursor()

passage = []

f = open(file = "D:\python\day10\信息",mode="r+",encoding="utf-8")
data = f.readlines()
for i in data:
    da = i.replace("\n","").split(",")
    passage.append(da)

    sql = "insert into user1(姓名,年龄,净资产) values(%s,%s,%s)"
    parm = [da[0],da[1],da[2]]
    cursor.execute(sql,parm)
    con.commit()
    f.close()

sql1 = "select sum(净资产) from user1"
cursor.execute(sql1)
sum = cursor.fetchall()
print("所有人的资产总和为：",sum[0])

cursor.close()
con.cursor()

# 二
f = open(file="x.jpg",mode="rb")
f1 = open(file="D:\python",mode="wb")
data = f.readline()
f1.write(data)
f1.close()
f.close()

# 三
print("请输入您身份证件的位置:")
add = input()
print("请输入您的身份证号：")
i= input()
address = "D:\python" + "/"+i
f = open(file=add,mode="rb")
f2 = open(file=address,mode="wb")

data = f.readline()
f2.write(data)
f2.close()
f.close()

#五
num=0
f = open(file="scores.txt",mode="r+",encoding="utf-8")
f2 = open(file="scores1.txt",mode="w+",encoding="utf-8")
data = f.readlines()
for i in data:
    da = i.replace("\n","").split(" ")
    f2.write(da[0])
    f2.write(" ")
    da1 = da
    del da1[0]
    for i in da1:
        i = int(i)
        num = num +i

    f2.write(str(num))
    f2.write("\n")

f.close()
f2.close()