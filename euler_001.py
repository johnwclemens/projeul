#from __future__ import print_function
import sys
import os.path
import jwc_cmdArgs

# define default values for the optional command line arguments
DEFAULT_FACTORS = [3,5]
DEFAULT_MAX = 10

def problem():
    print(this)
    print(this, "From ProjectEuler.net Problem 1:")
    print(this, "Compute the sum of the multiples less than -m for the list of factors -f")
    
def usage():
    print(this, "Usage:", this, "[-m max] [-f factors]")
    print(this, "e.g. :", this, "-m 10 -f 3 5")
    print(this, "e.g. :", this, "-f 3 5 -m 10")
    print(this, "e.g. :", this, "-f 3 5")
    print(this, "e.g. :", this, "-m 10")
    print(this, "e.g. :", this, "\n")

# calculate the sum of the multiples for all the factors (less than the max multiple)
# each row of data prints the row number, a new multiple, and the sum of all the previous multiples including the current row
# print column names and the data rows with tabs so the data can be read by Excel to make a chart
def sum_multiples(max = DEFAULT_MAX, factors = DEFAULT_FACTORS):
    count, sum = 0, 0
    print("\nmax = ", max, ", factors = ", factors, sep='')
    print("  Count\tMultiples\tSum of Multiples")
    for i in range(factors[0], max):
        for j in range(0, len(factors)):
            if i % factors[j] == 0:
                count += 1
                sum += i
                print("%7d\t%9d\t%16d" % (count, i, sum))
                break
    return sum

#describe the solution
def solution(sum, m, f):
    print (this, "The sum of the multiples less than m =", m, "for the list of factors f =", f, "is", sum)
    print(this)

this = os.path.basename(sys.argv[0]) + ':'
problem()    
usage()
argMap = {}
jwc_cmdArgs.parse_cmd_line(argMap)
f = DEFAULT_FACTORS
m = DEFAULT_MAX
if 'f' in argMap:
    if len(argMap['f']) > 0:
        f = int(argMap['f'][0])
if 'm' in argMap:
    if len(argMap['m']) > 0:
        m = int(argMap['m'][0])

sum = sum_multiples(m , f)
solution(sum, m, f)

