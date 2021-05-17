import xlwt
wt = xlwt.Workbook()
sheet =wt.add_sheet("商品信息")
sheet.write(0,0,"美国空气")
sheet.write(0,1,199)
sheet.write(1,0,"印度神油")
sheet.write(1,1,19.9)
sheet.write(2,0,"卫龙面筋")
sheet.write(2,1,3.5)
sheet.write(3,0,"以色列导弹")
sheet.write(3,1,120000)
sheet.write(4,0,"可口可乐/提")
sheet.write(4,1,18.8)
sheet.write(5,0,"奥利给/斤")
sheet.write(5,1,999)
sheet.write(6,0,"含笑半步癫")
sheet.write(6,1,9999)
sheet.write(7,0,"忘情水")
sheet.write(7,1,12888)
sheet.write(8,0,"葵花宝典")
sheet.write(8,1,"无价，赠与有缘人")
wt.save("我的商城.xls")
import xlrd
rb = xlrd.open_workbook(filename="D:\py课件\day13\任务\商城.xlsx",encoding_override=True)
sheet1 = rb.sheet_by_index(0)
row = sheet1.nrows
col = sheet1.ncols
for i in range(row):
    print(sheet1.row_values(i))