def fact_num(n):
    if(n>1):
        return n*fact_num(n-1)
    else:
        return n

n=int(input("Enter a number:"))

print(" of",n,"is",fact_num(n))

