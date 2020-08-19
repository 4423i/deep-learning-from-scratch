# coding: utf-8
class Man:
    """サンプルクラス"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Initilized!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")
    
    def HowOld(self):
        print(self.age)

m = Man("David","17")
m.hello()
m.goodbye()
print(type(m.HowOld()))
type(Man("David",17).HowOld())