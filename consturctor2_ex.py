class person:
    name = ""
    age = 0
    def __init__(self,a,b):
        self.name = a
        self.age = b

    def shownName(self):
        print(self.name)

    def showAge(self):
        print(self.age)



person1 = person(100,"first")
person1.showAge()
person1.shownName()

person2 = person(200, "second")
person2.shownName()
person2.showAge()