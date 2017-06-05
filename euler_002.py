import sys
import os.path
import jwc_cmdArgs

#fibs = []
#evens = []
#odds = []
DEFAULT_M = 4000000
DEFAULT_N = 10
DEFAULT_Z = 0

def problem():
    print(this)
    print(this, "From ProjectEuler.net Problem 2:")
    print(this, "Compute the sum of all the even Fibonacci Numbers less than:", '{:,}'.format(DEFAULT_M))
    
def usage():
    print(this, "Usage:", this, "[-m max | -n fibN] [-z]")
    print(this, "e.g. :", this, "-m 35")
    print(this, "e.g. :", this, "-n 35")
    print(this, "e.g. :", this, "\n")

def print_header():
    print("  N           Fibonacci N               Sum Fibs              Odd Fibs           Sum Odd Fibs             Even Fibs          Sum Even Fibs")
    print("------------------------------------------------------------------------------------------------------------------------------------------")

def calc_c(t, i, g):
    c = g
    if t == 'n':
        c = i
#    if t == 'm':
#        c = g
#    elif t == 'n':
#        c = i
#    else:
#        c = g
    return c
    
def sum_fibs(n, t, z):
    if z == 0:
        i, f, g, s_f, s_e, s_o = -1, 0, 1, 0, 0, 0
    else:
        i, f, g, s_f, s_e, s_o =  0, 1, 1, 0, 0, 0
    print_header()
    c = calc_c(t, i, g)
    while c < n:
        i, f, g, s_f = i+1, g, f+g, s_f+g
#        fibs.append(f)
        if f % 2 == 1:
            s_o = s_o+f
#            odds.append(f)
            print("%3d %21d %22d %21d %22d" % (i, f, s_f, f, s_o))
        else:
            s_e = s_e+f
#            evens.append(f)
            print("%3d %21d %22d                                              %21d %22d" % (i, f, s_f, f, s_e))
        if t == 'm':
            c = g
        elif t == 'n':
            c = i
    return s_e
    
def solution(sum, type, num):
    if type == 'm':
        print(this, "The sum of the even Fibonacci Numbers less than:", '{:,}'.format(num), "is:", '{:,}'.format(sum))
    elif type == 'n':
        print (this, "The sum of the even Fibonacci Numbers over the first:", '{:,}'.format(num), "Fibonacci numbers is:", '{:,}'.format(sum))
    else:
        print(this, "ERROR - Invalid type!", type, "sum:", '{:,}'.format(sum), "num:", '{:,}'.format(num))
    print(this)

this = os.path.basename(sys.argv[0]) + ':'
problem()
usage()
argMap = {}
jwc_cmdArgs.parse_cmd_line(argMap)
type = 'm'
num = DEFAULT_M
if 'n' in argMap:
    type = 'n'
    if len(argMap['n']) > 0:
        num = int(argMap['n'][0])
elif 'm' in argMap:
    if len(argMap['m']) > 0:
        num = int(argMap['m'][0])
    
z = DEFAULT_Z
if 'z' in argMap:
    z = 1
sum = sum_fibs(num, type, z)
solution(sum, type, num)


###################################################################################################

#deprecated functions

###################################################################################################


def parse_cmd_line_A(argMap):
    argc = len(sys.argv)
    print("argc = ", argc, ", argv = ", sys.argv, sep='')
    for i in range(1, argc):
        for key in argMap:
            if sys.argv[i][0] == '-' and sys.argv[i][1] == key:
                argList = []
                while i + 1 < argc and sys.argv[i + 1][0] != '-':
                    i = i + 1
                    argList.append(int(sys.argv[i]))
                argList = sorted(argList)
                argMap[key] = argList
                print("argMap[", key, "] = ", argMap[key], sep='')

                
def sum_fib_less_than(m):
    if USE_FIB_0 == 1:
        i, f, g, s_f, s_e, s_o = -1, 0, 1, 0, 0, 0
    else:
        i, f, g, s_f, s_e, s_o = 0, 1, 1, 0, 0, 0
    print_header()
    while g < m:
        i, f, g, s_f = i+1, g, f+g, s_f+g
#        fibs.append(f)
        if f % 2 == 1:
            s_o = s_o+f
#            odds.append(f)
            print("%3d %22d %22d %22d %22d" % (i, f, s_f, f, s_o))
        else:
            s_e = s_e+f
#            evens.append(f)
            print("%3d %22d %22d                                               %22d %22d" % (i, f, s_f, f, s_e))
    return s_e

def sum_first_fib(n):
    if USE_FIB_0 == 1:
        i, f, g, s_f, s_e, s_o = -1, 0, 1, 0, 0, 0
    else:
        i, f, g, s_f, s_e, s_o = 0, 1, 1, 0, 0, 0
    print_header()
    while i < n:
        i, f, g, s_f = i+1, g, f+g, s_f+g
#        fibs.append(f)
        if f % 2 == 1:
            s_o = s_o+f
#            odds.append(f)
            print("%3d %22d %22d %22d %22d" % (i, f, s_f, f, s_o))
        else:
            s_e = s_e+f
#            evens.append(f)
            print("%3d %22d %22d                                              %22d %22d" % (i, f, s_f, f, s_e))
    return s_e
