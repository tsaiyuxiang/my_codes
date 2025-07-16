# pizza.py

import sys
import os
from tabulate import tabulate

len1 = len(sys.argv)
if len1 < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len1 > 2:
    print("Too many command-line arguments")
    sys.exit(1)

if ".csv" in sys.argv[1] :
    len2 = len(sys.argv[1])
    if sys.argv[1][len2-4:] != ".csv" :  # abc.csvw 非 csv, abc.csv才是
        print("Not a CSV file")
        sys.exit(1)
else :
    print("Not a CSV file")
    sys.exit(1)

if not os.path.exists(sys.argv[1]):
    print("File does not exist")
    sys.exit(1)

'''
table = [["spam",42],["eggs",451],["bacon",0]]
headers = ["item", "qty"]
print(tabulate(table, headers, tablefmt="grid"))
+--------+-------+
| item   |   qty |
+========+=======+
| spam   |    42 |
+--------+-------+
| eggs   |   451 |
+--------+-------+
| bacon  |     0 |
+--------+-------+
'''

headers = []
table = []
with open(sys.argv[1],"r") as f:
    i = 0
    for line in f:
        line = line.strip()
        if i == 0:
            for item in line.split(",",2):  # headers
                headers.append(item)
        else:
            table_item = []
            if line.count(",") == 2:
                for item in line.split(",",2): # table
                    table_item.append(item)
                table.append(table_item)
        i += 1
    #print(f"headers: {headers}")
    #print(f"table: {table}")
    print(tabulate(table, headers, tablefmt="grid"))

