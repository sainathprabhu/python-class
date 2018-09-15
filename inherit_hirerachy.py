class Base:
    def geta(self):
        return 10
    def getb(self):
        return 20


class Sum(Base):
    def sum(self):
        print(self.geta() + self.getb())


class Sub(Base):
    def sub(self):
        print(self.geta() - self.getb())


f1=Sum()
f1.sum()

f2=Sub()
f2.sub()