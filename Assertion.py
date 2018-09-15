
#assert is a keyword to check values before performing the operations

def multiplication(a,b):
    assert(a!=0), "cannot perform the operation"  #makes sure that a is not zero
    assert(b!=0), "cannot perform the operation"  #makes sure that b is not zero
    return(a*b)

print(multiplication(3,0))
#print(multiplication(0,2))
#print(multiplication(3,32))