def sum_all(*args):
    sum=0
    for i in args:
        sum+=i
    return(sum)

sum=sum_all(1,2,3,4,5,6)
print(sum)