def factor(n):
    f = [1]
    for i in range(2, n):
       if not (n % i):
            f.append(i)
    f.append(n)
    print("%d %d" % (n, len(f)), end=' ')
    print(f[0], end=' ')
    for i in range(1, len(f)):
        print(f[i], end=' ')
    print()
    
n = 360
for i in range(1, n+1):
    factor(i)

