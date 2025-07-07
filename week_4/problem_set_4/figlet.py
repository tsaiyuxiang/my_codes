# figlet.py 2025/07/08

import pyfiglet
import sys

# 查看 sys.argv 列表內容
'''
print("sys.argv 內容：", sys.argv)
try:
    # 第 1 個參數
    print("第 1 個參數：", sys.argv[1])
except IndexError:
    print("命令列參數太少")
'''

argv = []
for arg in sys.argv:
    argv.append(arg)
len_argv = len(argv)
font = pyfiglet.FigletFont.getFonts()

if len_argv == 2:
    exit(1)
elif len_argv == 3:
    if (argv[1] == r"-f") or (argv[1] == r"--font") :
        if argv[2] in font:
            pass
        else:
            exit(1)
    else :
        exit(1)

str = input("Input: ")

if len_argv == 1:
    f = pyfiglet.figlet_format(str)
elif len_argv == 3:
    f = pyfiglet.figlet_format(str, font=argv[2])

print("Output: ")
print(f)

