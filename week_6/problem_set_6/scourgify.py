# scourgify.py

import sys
import os
import re

len1 = len(sys.argv)
if len1 < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len1 > 3:
    print("Too many command-line arguments")
    sys.exit(1)
if not os.path.exists(sys.argv[1]):
    print(f"Could not read {sys.argv[1]}")
    sys.exit(1)

str_to_write = f"first,last,house\n"
with open(sys.argv[1],"r") as f:
    i = 0
    for line in f:
        if i != 0:
            last_name, first_name, house = line.strip().split(",",2)
            first_name = re.sub('"',"",first_name).strip()
            last_name = re.sub('"',"",last_name).strip()
            house = house.strip()
            str_to_write += f"{first_name},{last_name},{house}\n"
        i += 1
with open(sys.argv[2],"w") as f:
    f.write(str_to_write)

