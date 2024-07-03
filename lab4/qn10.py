def divide_and_remainder(a,b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q,r=divide_and_remainder(10,6)
print(f"quotient={q}, remainder={r}")