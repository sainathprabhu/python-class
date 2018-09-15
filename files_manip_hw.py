'''fn = open("a.txt", "rb+")
ln = open("b.txt", "rb+")
fstr = fn.read()
lstr = ln.read()
flen = len(fstr)
llen = len(fstr)
for i in range(lent)
 if i%2 == 0:
    evenf.seek(2, 0)
    evenf.write()'''


'''     ff.seek() - points the cursor to the specified place
        ff.read() - read from the file
        ff.write() - write to the file 
        ff.tell() - where the cursor is 
        ff.close() - closes the file
        ff.open() - opens the file'''

fuln = open("a.txt", "r")
fn = open("b.txt", "w")
ln = open("c.txt", "w")
data1 =[]
fulstr = fuln.read()
fullen = len(fulstr)
print(fulstr)
for i in range(fullen):
    if (i%2==0):
        fn.write(fulstr[i])
        data1.add(fulstr[1])
    else:
        ln.write(fulstr[i])
        data2.add(fulstr[i])

    '''if (i%2==0):
        #fuln.write()
        print(fulstr[i])'''