def apply_function(func, value):
    return func(value)

def add_one(x):
    return x + 1

result = apply_function(add_one, 5)
print(result)