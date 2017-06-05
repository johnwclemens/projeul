#from __future__ import print_function
import sys
import os.path

def factor(n):
    f = []
    print("[", end='')
    for i in range(1, n+1):
        f.append(i)
        if not (n % i):
#            print(','.join([f[b] for b in range(1, n)]))
#            '''
            # custom print [a b c d e] - python provides the '[' and ']' brackets
            if len(f) == 1:                     # print first element without any space
                print("%d" % (f[i-1]), end='')
            else:                               # print a space before each of the remaining elements
                print(" %d" % (f[i-1]), end='')
#            '''
    print("]")
factor(60)
