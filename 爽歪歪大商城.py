print("------------欢迎来到爽歪歪大商城-------------")
import random
coupon = (random.randint(1,30))
coupon = int(coupon)
if coupon <= 10:
        print("恭喜获得一张辣条优惠券：满600减300")
elif coupon > 10:
        print("获得lenovo优惠券：半价优惠")
else:
        print("抱歉，活动结束!")

shop = [
    ["lenovo thinkpad e580",5000],
    ["ipad 2021",3000],
    ["华为手表",3000],
    ["辣条",3.5],
    ["大米",50],
    ["旺财QQ糖",50],
    ["防盗内裤",150],
    ["电磁波秋裤",320],
    ["忘情水",999],
    ["呼伦贝尔新鲜空气",100],
    ["烤山药",4.5]
]
salary = a  = input("请输入您的薪资：")
salary = int(salary)
a = int(a)
mycart = []

while True:
    for index,value in enumerate(shop):
        print(index,"  ",value)
    num = input("请输入您要买的商品编号：")
    if num.isdigit():
        num = int(num)
        if num >= len(shop):
                print("看不见编号最大多少？重新输入，听明白了没有!")
        else:
            if salary >= shop[num][1]:
                    mycart.append(shop[num])
                    salary = salary - shop[num][1]

                    print("成功添加到购物车！！！余额为：", salary)
            else:
                    print("充钱，穷鬼，您的金额不足，能明白意思吧!")
    elif num == "Q" or num == "q":
          print("---------------------------***欢迎下次光临！！！！-------------------------------")
          break
    else:
          print("输入非法！！！！请重新输入！！！")

print("您本次购物商品如下：")
for index, value in enumerate(mycart):
    print(index, "  ", value)
print("您消费：",a-salary,"您的余额为：", salary,"你的积分为:",(a-salary)//10,
	  "满999积分凭小票可上顶楼享受一套一条龙服务,嘻嘻，死鬼。")
import datetime
time = datetime.datetime.now()
print("------------------------------",time,"-------------------------------")

while True:
    jifen = input("是否兑换服务套票(1:换，2：退出)：")
    jifen = int(jifen)
    if (a-salary)//10>=999 and jifen == 1:
        print("兑换成功!还剩余积分:",(a-salary)//10-999)
        break
    elif (a-salary)//10 < 999 and jifen == 1:
        print("积分不够！！！2：退出！")
    else:
        print("拜拜了您嘞")
        break