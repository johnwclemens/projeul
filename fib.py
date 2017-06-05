def fib1(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    a, b = 0, 1
    for i in range(n):
        print("[%3d] %d"% (i, a))
        a, b = b, a+b
    print()

a = 400
fib1(a)
fib2(a)
