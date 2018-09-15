n = 10
num = 1
for row in range(1,11):
    #for col in range(0,1):
        if row % 2 == 0:        #prints for 2st row
            print("\t", num)
        elif row % 3 == 0:      #prints for 3st row
            print("\t","\t",num)
        else:                   #prints for 1st row
            print(num)
        num = num +1