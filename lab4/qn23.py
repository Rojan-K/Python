def power(b,p):
    if p==0:
        return 1
    elif p==1:
        return b
    else:
        return b*power(b,p-1)

b=int(input("Enter a base value:"))
p=int(input("Enter a power value:"))
ans=power(b,p)
print(f"{b}^{p}=={ans}")