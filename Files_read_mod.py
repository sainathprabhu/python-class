ff=open("b.txt", "r")
print(ff.tell())
str=ff.read()#you can define to read certain charaters by defining it in read(10)
print(ff.tell())#tells the
print(len(str))
print(str)
