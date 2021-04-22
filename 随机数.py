import random
num = random.randint(0,100)
count = 0
coin = 5000
while count <=6:
    count = count + 1
    coin = coin - 500
    print("第",count,"次")
    print("还剩",coin,"币")
    a = input("你要猜的数：")
    a = int(a)
    if a > num:
        print("大了")
    elif a < num:
        print("小了")
    else:
        print("恭喜你")
        break
