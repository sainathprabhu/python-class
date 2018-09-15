def fact(n) -> object:
    if(n==1):
        return 1
    else:
        return n*fact(n-1)

a=int(input("enter the value ="))
print(fact(a))