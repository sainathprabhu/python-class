try:
    a =10
    b = 0
    c = a/b
    print(c)
except ZeroDivisionError: #will print if there is any exception
    print("ZeroDivisionError Occured")
except TypeError:
    print("Type Error")
except Exception:
    print("Some Error")
finally:                        #this will be executed after exception or try block
    print("connection closed")