def sum_of_digit(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digit(n // 10)
n=int(input("Enter a number:"))
sum=sum_of_digit(n)
print("Sum of digit of number ",sum)