#1号服装
day1="1号"
name1="羽绒服"
price1=253.6
QTY1=500
sales1=10

#2号服装
day2="2号"
name2="牛仔裤"
price2=86.3
QTY2=600
sales2=60

#3号服装
day3="3号"
name3="风衣"
price3=96.8
QTY13=335
sales3=43

#4号服装
day4="4号"
name4="皮草"
price4=135.9
QTY4=855
sales4=63

#5号服装
day5="5号"
name5="T恤"
price5=65.8
QTY5=632
sales5=63

#6号服装
day6="6号"
name6="衬衫"
price6=49.3
QTY6=562
sales6=120

#7号服装
day7="7号"
name7="牛仔裤"
price7=86.3
QTY7=600
sales7=72

#8号服装
day8="8号"
name8="羽绒服"
price8=253.6
QTY8=500
sales8=69

#9号服装
day9="9号"
name9="牛仔裤"
price9=86.3
QTY9=600
sales9=35

#10号服装
day10="10号"
name10="羽绒服"
price10=253.6
QTY10=500
sales10=140

#11号服装
day11="11号"
name11="牛仔裤"
price11=86.3
QTY11=600
sales11=90

#12号服装
day12="12号"
name12="皮草"
price12=135.9
QTY12=855
sales12=24

#13号服装
day13="13号"
name13="T恤"
price13=65.8
QTY13=632
sales13=45

#14号服装
day14="14号"
name14="风衣"
price14=96.8
QTY14=335
sales14=25

#15号服装
day15="15号"
name15="牛仔裤"
price15=86.3
QTY15=600
sales15=60

#16号服装
day16="16号"
name16="T恤"
price16=65.8
QTY16=632
sales16=129

#17号服装
day17="17号"
name17="羽绒服"
price17=253.6
QTY17=500
sales17=10

#18号服装
day18="18号"
name18="风衣"
price18=96.8
QTY18=335
sales18=43

#19号服装
day19="19号"
name19="T恤"
price19=65.8
QTY19=632
sales19=63

#20号服装
day20="20号"
name20="牛仔裤"
price20=86.3
QTY20=600
sales20=60

#21号服装
day21="21号"
name21="皮草"
price21=135.9
QTY21=855
sales21=63

#22号服装
day22="22号"
name22="风衣"
price22=96.8
QTY22=335
sales22=60

#23号服装
day23="23号"
name23="T恤"
price23=65.8
QTY23=632
sales23=58

#24号服装
day24="24号"
name24="牛仔裤"
price24=86.3
QTY24=600
sales24=140

#25号服装
day25="25号"
name25="T恤"
price25=65.8
QTY25=632
sales25=48

#26号服装
day26="26号"
name26="风衣"
price26=96.8
QTY26=335
sales26=43

#27号服装
day27="27号"
name27="皮草"
price27=135.9
QTY27=855
sales27=57

#28号服装
day28="28号"
name28="羽绒服"
price28=253.6
QTY28=500
sales28=10

#29号服装
day29="29号"
name29="T恤"
price29=65.8
QTY29=632
sales29=63

#30号服装
day30="30号"
name30="风衣"
price30=96.8
QTY30=335
sales30=78

#羽绒服销售数量a
a = (sales1+sales8+sales10+sales17+sales28)
print(a)
#牛仔裤销数量b
b = (sales2+sales7+sales9+sales11+sales15+sales20+sales24)
print(b)
#风衣销售数量c
c = (sales3+sales14+sales18+sales22+sales26+sales30)
print(c)
#皮草销售数量d
d = (sales4+sales12+sales21+sales27)
print(d)
#T恤销售数量e
e = (sales5+sales13+sales16+sales19+sales23+sales25+sales29)
print(e)
#衬衫销售数量f
f = sales6
print(f)
print("总销售数量：",(a+b+c+d+e+f))

#羽绒服销售占比
print (round(a/(a+b+c+d+e+f),2))
#牛仔裤销售占比
print (round(b/(a+b+c+d+e+f),2))
#风衣销售占比
print (round(c/(a+b+c+d+e+f),2))
#皮草销售占比
print (round(d/(a+b+c+d+e+f),2))
#T恤销售占比
print (round(e/(a+b+c+d+e+f),2))
#衬衫销售占比
print (round(f/(a+b+c+d+e+f),2))

#羽绒服销售额a1
a1 = (price1*(sales1+sales8+sales10+sales17+sales28))
print("￥",a1)
#牛仔裤销售额b1
b1 = (price2*(sales2+sales7+sales9+sales11+sales15+sales20+sales24))
print("￥",b1)
#风衣销售额c1
c1 = (price3*(sales3+sales14+sales18+sales22+sales26+sales30))
print("￥",c1)
#皮草销售额d1
d1 = round(price4*(sales4+sales12+sales21+sales27),1)
print("￥",d1)
#T恤销售额e1
e1 = round(price5*(sales5+sales13+sales16+sales19+sales23+sales25+sales29),1)
print("￥",e1)
#衬衫销售额f1
f1 = (price6*sales6)
print("￥",f1)
print("总销售额：￥",(a1+b1+c1+d1+e1+f1))

#羽绒服销售额占比
print (round(a1/(a1+b1+c1+d1+e1+f1),2))
#牛仔裤销售额占比
print (round(b1/(a1+b1+c1+d1+e1+f1),2))
#风衣销售额占比
print (round(c1/(a1+b1+c1+d1+e1+f1),2))
#皮草销售额占比
print (round(d1/(a1+b1+c1+d1+e1+f1),2))
#T恤销售额占比
print (round(e1/(a1+b1+c1+d1+e1+f1),2))
#衬衫销售额占比
print (round(f1/(a1+b1+c1+d1+e1+f1),2))
