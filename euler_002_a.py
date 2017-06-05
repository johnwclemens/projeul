import sys

args = []
fibs = []
evens = []
odds = []
USE_FIB_0 = 1

def fib_less_than(n):
    if USE_FIB_0 == 1:
        a, b = 0, 1
    else:
        a, b = 1, 1
    while b < n:
#        print(a, end=' ')
        a, b = b, a+b
        fibs.append(a)
        if a % 2 == 0:
            evens.append(a)
        else:
            odds.append(a)
#    print()

def fib_index(n):
    if USE_FIB_0 == 1:
        a, b = 0, 1
    else:
        a, b = 1, 1
    for i in range(n):
#        print("[%3d] %d"% (i, a))
        a, b = b, a+b
        fibs.append(a)
        if a % 2 == 0:
            evens.append(a)
        else:
            odds.append(a)
#    print()

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
            
argc = parseArgs()
print("argc=", argc, ", args=", args, sep='')

fib_less_than(args[1])
print("fibs=", fibs)

min = 1
if USE_FIB_0 == 1:
    min = 0

for i in range(min, len(fibs)):
    print("fib[", i, "] = ", fibs[i], sep='')
print("odds = ", odds)
print("evens = ", evens)

sum_ = 0
for i in fibs:
    sum_ += i
print("The sum of all the fibs less than ", args[1], " equals ", sum_)

sum_ = 0
for i in odds:
    sum_ += i
print("The sum of the odd fibs less than ", args[1], " equals ", sum_)

sum_ = 0
for i in evens:
    sum_ += i
print("The sum of the even fibs less than ", args[1], " equals ", sum_)
