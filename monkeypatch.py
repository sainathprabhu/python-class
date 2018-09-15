import m


class monkeyf:
    def monkey_f(self):
        print("monkey_f()")


m.Myclass.f = monkey_f()
obj = m.Myclass()
obj.f()
