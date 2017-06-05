import sys

args = []
fibs = []
evens = []
odds = []
USE_FIB_0 = 1

def parseArgs():
    argc = len(sys.argv)
    args.append(sys.argv[0])
    for i in range(1, argc):
         try:
             args.append((int)(sys.argv[i]))
         except ValueError:
             print("ValueError! Exception Caught in parseArgs(", sys.argv[i], ")", sep="'")
             usage()
#         except:
#             print("Uexpected Error!", sys.api_version.exc_info()[0])
#             raise
    return argc
            
def fib_less_than(m):
    if USE_FIB_0 == 1:
        c, f, g, s_f, s_e, s_o = -1, 0, 1, 0, 0, 0
    else:
        c, f, g, s_f, s_e, s_o = 0, 1, 1, 0, 0, 0
    print("  N  Fibonacci N    Sum Fib N      Odd Fib   SumOddFib     EvenFib  SumEvenFib")
    print("-----------------------------------------------------------------------------")
    while g < m:
        c, f, g, s_f = c+1, g, f+g, s_f+g
        fibs.append(f)
        if f % 2 == 1:
            s_o = s_o+f
            odds.append(f)
            print("%3d %12d %12d %12d %12d" % (c, f, s_f, f, s_o))
        else:
            s_e = s_e+f
            evens.append(f)
            print("%3d %12d %12d                       %12d %12d" % (c, f, s_f, f, s_e))
#            print("-----------------------------------------------------------------------------")

def fib_num(n):
    if USE_FIB_0 == 1:
        f, g, s_f, s_e, s_o = 0, 1, 0, 0, 0
    else:
        f, g, s_f, s_e, s_o = 1, 1, 0, 0, 0
    for i in range(n):
#        print("[%3d] %d"% (i, a))
        f, g, s_f = g, f+g, s_f+g
        fibs.append(f)
        if f % 2 == 1:
            s_o = s_o+f
            odds.append(f)
            print("%3d %12d %12d %12d %12d" % (i, f, s_f, f, s_o))
        else:
            s_e = s_e+f
            evens.append(f)
            print("%3d %12d %12d                       %12d %12d" % (i, f, s_f, f, s_e))

argc = parseArgs()
print("argc=", argc, ", args=", args, sep='')
fib_less_than(args[1])
fib_num(args[1])
