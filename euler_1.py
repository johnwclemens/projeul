import sys
h = {}
def fact(a, b, n):
    print("fact() a=", a, ", b=", b, ", n=", n, sep='')
    f = (a, b)
    print("f=", f)
    g = []
    sum = 0
    size = 0
    for i in range(1, n):
#        if not ((i % f[0]) and (i % f[1])):
        if i % f[0] == 0 or i % f[1] == 0:
            g.append(i)
            sum += i
            size = len(g)
        print("i=", i, ", g[", size, "] = ", g, " ", sum, sep='')
    print("euler #1:", sum)
   
def parseArgs():
    args = str(sys.argv)
    print(args)
    argc = len(sys.argv)
    for i in range(1, argc):
        h[i] = (int)(sys.argv[i])
    print("parseArgs() a=", h[1], ", b=", h[2], ", n=", h[3])
            
parseArgs()
fact(h[1], h[2], h[3])
