def make_multiplier(n):
    def multiplier(x):
        return n*n
    return multiplier(n)

mu=make_multiplier(7)
print(mu)