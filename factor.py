################################################################################################################################ 
import sys

def factor(n):                                                  #n: assume n is an integer?
    f = []                                                      #f: list of factors for the number n
    s = 1                                                       #s: sign of the number n, default = 1 i.e. positive
    if n < 0:                                                   #if n is negative
        s = -1                                                  #then s and sign are negative
    for i in range(s, n + s, s):
        if not (n % i):     #if n % i != 0
            f.append(i)
    print(n, len(f), end=' [')
    if n != 0:
        print(f[0], end='')
    for i in range(1, len(f)):
        print(" %d" % (f[i]), end='')
    print(']')

    return len(f)

argc = len(sys.argv)
args = str(sys.argv)
print(args)

print(sys.argv[0], argc - 1, end=' : [ ')
for i in range(1, argc):
    print("%s " % (sys.argv[i]), end='')
print(']')

n_f = {} #
f_n = {}
_max = 0
n = 60
if argc == 2:
    n = (int)(sys.argv[1])
s = 1
if n < 0:
    s = -1
for i in range(s, n + s, s):
    tmp = factor(i)
    if tmp > _max:
        _max = tmp
        f_n[i] = _max;
        n_f[_max] = i
        
print("raw f_n()", f_n)
print("f_n.keys()", sorted(f_n.keys()))
print("f_n.values()", sorted(f_n.values()))
print("raw  n_f()", n_f)
print("n_f.keys()", sorted(n_f.keys()))
print("n_f.values()", sorted(n_f.values()))
print('good bye')
