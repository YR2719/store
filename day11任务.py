class cup:
    color = ""
    size = ""
    hight = 0
    caizhi = ""
    ability = ""

    def run(self):
        print(self.color,"的杯子,","高:",self.hight,"能装",self.size,"的液体,材质是",self.caizhi,",注意：",c.ability)

c = cup()
c.color = "白色"
c.size = "500ml"
c.hight = "12cm"
c.caizhi = "新型合成材料"
c.ability = "不能装温度超过200度或有腐蚀性液体！"
c.run()


class computer:
    __size = ""
    __price = 0
    __cpu = ""
    __neicun = ""
    __time = 0
    def setSize(self,size):
        self.__size = size
    def getSize(self,size):
        return self.__size
    def setPrice(self,price):
        self.__price = price
    def getPrice(self,price):
        return self.__price
    def setCPU(self,cpu):
        self.__cpu = cpu
    def getCPU(self,cpu):
        return self.__cpu
    def setNeicun(self,neicun):
        self.__neicun = neicun
    def getNeicun(self,neicun):
        return self.__neicun
    def setTime(self,time):
        self.__time = time
    def getTime(self,time):
        return self.__time
    def type(self,num):
        print("打了",num,"个字")
    def playgame(self,gamename):
        print("正在打",gamename)
    def watch(self,watchwhat):
        print("正在看",watchwhat)

    def show(self):
        print("这是一台",self.__size,"的电脑，价值",self.__price,"拥有",self.__cpu,
              "的cpu和",self.__neicun,"的内存，它可以待机",self.__time,"小时。")

a = computer()
a.setSize ("7寸")
a.setPrice (12000)
a.setCPU ("G6405")
a.setNeicun ("1T")
a.setTime (3)
a.show()
