# lines.py
import sys
import os

len1 = len(sys.argv)
if len1 < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len1 > 2:
    print("Too many command-line arguments")
    sys.exit(1)

if ".py" in sys.argv[1] :
    len2 = len(sys.argv[1])
    if sys.argv[1][len2-3:] != ".py" :  # abc.pyh 非 python, abc.py才是
        print("Not a Python file")
        sys.exit(1)
else :
    print("Not a Python file")
    sys.exit(1)

if not os.path.exists(sys.argv[1]):
    print("File does not exist")
    sys.exit(1)

code_line_count = 0
with open(sys.argv[1],"r") as f:
    for line in f:
        line = line.strip()
        len_line = len(line)
        #print(f"{len_line},({line[0:1]})")
        if (len_line > 0) and (line[0:1] != "#") :
            code_line_count += 1
print(code_line_count)




