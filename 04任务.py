City = ["北京","上海","天津","重庆","哈尔滨","长春","沈阳","呼和浩特","石家庄","乌鲁木齐","兰州","西宁",
     "西安","银川","郑州","济南","太原","合肥","长沙","武汉","南京","成都","贵阳","昆明","南宁","拉萨","杭州",
     "南昌","广州","福州","台北","海口"]
City.append("香港")
City.append("澳门")
print(City)
City.remove("广州")
print(City)
City.insert(1,"广州")
print(City)


GDP = [36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
total = sum(GDP)
print(round(total,2))
mean = (total/(len(GDP)))
print(round(mean,2))

a = [1,5,21,30,15,9,30,24]
sum1 = 0
for A in (a):
     if A%5 == 0:
      sum1 += A
print(sum1)


#list = [1,2,3,4,5,6,7,8,9]
#实现效果：list = [9,8,7,6,5,4,3,2,1]

list = [1,2,3,4,5,6,7,8,9]
list.reverse()
print(list)


from collections import Counter
a = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
result = Counter(a)
print (result)