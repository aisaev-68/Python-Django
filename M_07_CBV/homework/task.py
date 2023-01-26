def multiply(num1):
    var = 10
    def inner(num2):
        return num1 * num2
    return inner


mult_by_9 = multiply(9)

print(mult_by_9)
print(mult_by_9.__closure__)
print(mult_by_9.__closure__[0].cell_contents)
print(mult_by_9(9))
print(mult_by_9(3))