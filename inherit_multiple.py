class Base1:
    def geta(self):
        return 10


class Base2:
    def getb(self):
        return 20


class Sum(Base1, Base2):
    def sum(self):
        print(self.geta() + self.getb())


x = Sum()
x.sum()
