import re
import sys
import os.path
import inspect

inLineNum, outLineNum = 0, 0
comment = "//c2g//"
WCL = True
outFile = open("tmain.log", "w")

def main():
    global inLineNum
    inLineNum += 1
    print("hello world")
    pattern = r'u'
    line = "hello world\n"
    (ret, outLine) = removePattern(pattern, line)
    (ret, outLine) = (True, outLine) if ret else removePattern(pattern, line)
    print("%d: ret=%d outLine='%s'" % (lineNum(), ret, outLine))
#    outLine = removePattern(pattern, line)
#    print("%d: outLine: '%s'" % (lineNum(), outLine))

def lineNum():
    return inspect.currentframe().f_back.f_lineno

def getCaller():
    return inspect.stack()[2][3] + "()"

def removePattern(pattern, line, flag=True):
    global outLineNum
    outLine = ''
    m = re.search(pattern, line)
    if m:
        print("%d: removePattern(%s)[%d] MATCHED RE: %s:" % (lineNum(), getCaller(), flag, pattern))
        print("%d: <-[%d] '%s'" % (lineNum(), inLineNum, line))
        if WCL:
            dbgLine = comment + line
            outFile.write(dbgLine + "\n")
            outLineNum += 1
            print("%d: ->[%d] '%s'" % (lineNum(), outLineNum, dbgLine))
        outLine = re.sub(pattern, '', line)
    return (True, outLine) if m else (False, outLine)

def removePattern_OLD(pattern, line, flag=True):
    global outLineNum
    outLine = ''
    m = re.search(pattern, line)
    if m:
        print("%d: removePattern(%s)[%d] MATCHED RE: %s:" % (lineNum(), getCaller(), flag, pattern))
        print("%d: <-[%d] '%s'" % (lineNum(), inLineNum, line))
        if WCL:
            dbgLine = comment + line
            outFile.write(dbgLine + "\n")
            outLineNum += 1
            print("%d: ->[%d] '%s'" % (lineNum(), outLineNum, dbgLine))
        outLine = re.sub(pattern, '', line)
    if flag:
        return True if m else False
    else:
        print("%d: removePattern() outLine='%s'" % (lineNum(), outLine))
    return outLine

if __name__ == '__main__':
    main()
