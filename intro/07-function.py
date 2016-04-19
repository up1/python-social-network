def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

def modulus(x, y):
    return x % y

def exponent(x, y):
    return x**y


print "%d plus %d is %d" % (20, 10, addition(20, 10))
print "%d minus %d is %d" % (20, 10, subtraction(20, 10))
print "%d mulpliply by %d is %d" % (20, 10, multiplication(20, 10))
print "%d divide by %d is %d" % (20, 10, division(20, 10))
print "%d modulo by %d is %d" % (20, 10, modulus(20, 10))
print "%d power by %d is %d" % (20, 10, exponent(20, 10))
