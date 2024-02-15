x = lambda a,b : a * b
print(x(5,6))

def myfunc(num):
    return lambda a :a * num

square = myfunc(2)

print(square)