class Base:
    def geta(self):
        return 10

    def getb(self):
        return 20


class Drived1(Base):
    def sum(self):
        return (self.geta() + self.getb())


class Drived2(Base):
    def sub(self):
        return (self.geta() - self.getb())


class LastDrived(Drived1, Drived2):
    def avg(self):
        print(self.sum() + self.sub() / 2)


ld = LastDrived()
ld.avg()
