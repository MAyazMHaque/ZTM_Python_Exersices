## this is the list method:

def fibonacci(num):
    a = 0
    b = 1
    fib = []
    for i in range(num):
        fib.append(a)
        a_old = a
        a = b
        b = a_old + b

    return fib


print(fibonacci(1000))


## Now using the range method:

def fibonacci2(num):
    a2 = 0
    b2 = 1
    for i in range(num):
        yield a2
        old_a2 = a2
        a2 = b2
        b2 = old_a2 +b2

for x in fibonacci2(1000):
    print(x)