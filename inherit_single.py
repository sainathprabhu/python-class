class Base:
    def geta(self):
        return 10
    def getb(self):
        return 30

class Derived(Base):
    def sum(self):
        print(self.geta()+self.getb())

d=Derived()
d.sum()