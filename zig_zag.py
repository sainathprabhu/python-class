n = 10
num = 1
for row in range(1,11):
    for col in range(0,1):
        if row % 2 == 0:
            print("\t", num)
        else:
            print(num)
        num = num +1