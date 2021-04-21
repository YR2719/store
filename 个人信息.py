IDnumber = input("请输入你的身份证编号")
name = input("请输入你的名字")
age = input("请输入你的年龄")
sex = input("请输入你的性别")
hight = input("请输入你的身高")
add = input("请输入你的居住地址")

info='''
---------------个人信息----------------
身份证号：%s
名字：   %s
年龄：   %s
性别：   %s
身高：   %s
居住地址：%s
-------------------------------------
'''
print(info % (IDnumber,name,age,sex,hight,add))