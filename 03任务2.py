sum = 0
sum1 = 0
while sum <= 99:
    sum = sum + 1
    sum1 += sum

print(sum1)


hight = 20
day = 3
night = 2
count = 0
while True:
    count = count + 1
    if day * count - night * (count-1) >= hight:
     print("需要",count,"天")
     break

