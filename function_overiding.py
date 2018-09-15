class Base:
    a =10
    def geta(self):
        return self.a
    def getb(self):
        return 20

class Drived1(Base):
    def geta(self):
        return 100
    def sum(self):
        return(self.geta()+self.geta()+self.getb())


d1=Drived1()
print(d1.sum())