class student:
    def display(self, a):
        print(a)
        print("simple print")


s = student()
s.display(10)
# student().display(10) > this not recommended as it consumes more memory when called many times
