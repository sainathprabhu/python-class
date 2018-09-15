ff=open("b.txt","r")
ff.seek(2,0)#starts the cursor from 0th line 2nd line
str=ff.read()
#print(ff.tell())
print(str)
ff.close()