def outer_function():
    def inner_function():
        return "Hello"
    return inner_function()

str=outer_function()
print(str)