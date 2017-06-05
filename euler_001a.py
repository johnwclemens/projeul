import sys
import os.path

# define default values for the optional command line arguments
DEFAULT_FACTORS = [3,5]
DEFAULT_MAX = [1000]

# it is customary to print the usage syntax for programs that take command line arguments
# the '[]' denote optional arguments (they do not need to be used)
# if the -m argument is not given, then the default value of DEFAULT_MAX is used
# if the -f arguments are not given, then the default values of DEFAULT_FACTORS are used
def usage():
    print("\nUsage:", sys.argv[0], "[-m max] [-f factors]")
    print("e.g. :", sys.argv[0], "-m 10 -f 3 5")
    print("e.g. :", sys.argv[0], "-f 3 5 -m 10")
    print("e.g. :", sys.argv[0], "-f 3 5")
    print("e.g. :", sys.argv[0], "-m 10")
    print("e.g. :", sys.argv[0], "\n")

# calculate the sum of the multiples for all the factors (less than the max multiple)
# each row of data prints the row number, a new multiple, and the sum of all the previous multiples including the current row
def sum_multiples(max = DEFAULT_MAX, factors = DEFAULT_FACTORS):
    count, sum = 0, 0
    if len(max) <= 0:
        max = DEFAULT_MAX
    if len(factors) <= 0:
        factors = DEFAULT_FACTORS
    print("\nmax = ", max, ", factors = ", factors, sep='')
# print column names and the data rows with tabs so the data can be read by Excel to make a chart
    print("   Count\tMultiples\t\t     Sum")
    for i in range(factors[0], max[0]):
        for j in range(0, len(factors)):
            if i % factors[j] == 0:
                count += 1
                sum += i
                print("%8d\t%8d\t%16d" % (count, i, sum))
                break
    return sum

def parse_cmd_line(argMap):
    argc = len(sys.argv)
    dir = os.path.dirname
    file = os.path.basename
    print("path = ", path, ", file = ", file)
    print("argc = ", argc, ", ", sys.argv, sep='')
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

# describe the problem
def problem():
    print ("\nCompute the sum of all the multiples less than -m for for the list of factors -f")
    
#describe the solution
def solution(sum):
    print ("The sum of all the multiples less than -m for the list of factors -f is ", sum)

problem()    
usage()
#'_p':'', '_q':'', 
argMap = {'f':'', 'm':''}
parse_cmd_line(argMap)
sum = sum_multiples(argMap['m'] , argMap['f'])
solution(sum)
