def multiply(*args):
    mul=1
    for i in args:
        mul*=i
    return(mul)

m=multiply(1,2,3)
print(m)