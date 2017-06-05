import os
import shlex
import platform
import struct
import subprocess
import colorama
from colorama import win32

ESC = "\033"
COLORS = {'B_B':colorama.Back.BLACK, 'B_W':colorama.Back.WHITE, 'B_R':colorama.Back.RED, 'B_G':colorama.Back.GREEN, 'B_U':colorama.Back.BLUE, 'B_Y':colorama.Back.YELLOW, 'B_C':colorama.Back.CYAN, 'B_M':colorama.Back.MAGENTA, 
          'F_B':colorama.Fore.BLACK, 'F_W':colorama.Fore.WHITE, 'F_R':colorama.Fore.RED, 'F_G':colorama.Fore.GREEN, 'F_U':colorama.Fore.BLUE, 'F_Y':colorama.Fore.YELLOW, 'F_C':colorama.Fore.CYAN, 'F_M':colorama.Fore.MAGENTA}

def main():
    colorama.init(autoreset=True)
    clearScreen()
    print(COLORS['B_B'] + COLORS['F_W'] + "%s[%s;%sH%s" % (ESC, 2, 1, 'X'))
    print(COLORS['B_G'] + COLORS['F_W'] + "%s[%s;%sH%s" % (ESC, 2, 2, 'X'))
    print(COLORS['B_U'] + COLORS['F_W'] + "%s[%s;%sH%s" % (ESC, 2, 3, 'X'))
    print(COLORS['B_R'] + COLORS['F_W'] + "%s[%s;%sH%s" % (ESC, 2, 4, 'X'))
    print(COLORS['B_C'] + COLORS['F_W'] + "%s[%s;%sH%s" % (ESC, 2, 5, 'X'))
    print(COLORS['B_Y'] + COLORS['F_W'] + "%s[%s;%sH%s" % (ESC, 2, 6, 'X'))
    print(COLORS['B_M'] + COLORS['F_W'] + "%s[%s;%sH%s" % (ESC, 2, 7, 'X'))
    print(COLORS['B_W'] + COLORS['F_W'] + "%s[%s;%sH%s" % (ESC, 2, 8, 'X'))

    print(COLORS['B_B'] + COLORS['F_B'] + "%s[%s;%sH%s" % (ESC, 3, 1, 'X'))
    print(COLORS['B_B'] + COLORS['F_G'] + "%s[%s;%sH%s" % (ESC, 3, 2, 'X'))
    print(COLORS['B_B'] + COLORS['F_U'] + "%s[%s;%sH%s" % (ESC, 3, 3, 'X'))
    print(COLORS['B_B'] + COLORS['F_R'] + "%s[%s;%sH%s" % (ESC, 3, 4, 'X'))
    print(COLORS['B_B'] + COLORS['F_C'] + "%s[%s;%sH%s" % (ESC, 3, 5, 'X'))
    print(COLORS['B_B'] + COLORS['F_Y'] + "%s[%s;%sH%s" % (ESC, 3, 6, 'X'))
    print(COLORS['B_B'] + COLORS['F_M'] + "%s[%s;%sH%s" % (ESC, 3, 7, 'X'))
    print(COLORS['B_B'] + COLORS['F_W'] + "%s[%s;%sH%s" % (ESC, 3, 8, 'X'))

    csbi = win32.CONSOLE_SCREEN_BUFFER_INFO()
    print(csbi)

#    size = getTermSize()
#    print('term size={}'.format(size))
    
def getTermSize():
    os = platform.system()
    size = None
    if os == 'Windows':
        xy = getTermSizeWindows()
    if size is None:
        size = (80, 25)
    return size
    
def getTermSizeWindows():
    try:
        print('before import')
        from ctypes import windll, create_string_buffer
        print('after import, before GetStdHandle()')
        h = windll.kernal32.GetStdHandle(-12)
        print('after GetStdHandle({}), before create_string_buffer()'.format(h))
        strBuff = create_string_buffer(22)
        print('after create_string_buffer({}), before GetConsoleScreenBufferInfo()'.format(strBuff))
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, strBuff)
        print('after GetConsoleScreenBufferInfo({})'.format(res))
        if res:
            (bufx, bufy, curx, cury, wattr, left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", strBuff.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
            return sizex, sizey
    except Exception as e:
        print('getTermSizeWindows() Exception:{}'.format(e))
          
def moveTo(row, col):
    if row > 0 and col > 0:
        print("%s[%s;%sH" % (ESC, row, col), end='')
    else:
        info = 'Exception in moveTo({:d},{:d})'.format(row, col)
        printe(info, 1, 1)
            
def prints(c, row, col, colors=COLORS['B_B'] + COLORS['F_R']):
    global g_outFile
    print(colors + "%s[%s;%sH%s" % (ESC, row, col, str(c)), end='')
    if g_outFile:
        print(colors + "%s[%s;%sH%s" % (ESC, row, col, str(c)), end='', file=g_outFile)

def printe(c, row=1, col=1, colors=COLORS['B_C'] + COLORS['F_R']):
    global g_endRow
    print(colors +  "%s[%s;%sH%s" % (ESC, g_endRow, 1, str(c)), end='')
    moveTo(row, col)
    g_endRow += 1

def clearScreen():
    print("%s[2J" % (ESC))

if __name__ == "__main__":
    main()
