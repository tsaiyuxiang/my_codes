# twttr.py

import re

if __name__ == "__main__":
    str1 = input("Input: ")
    str1 = re.sub(r"[AEIOUaeiou]", r"", str1)
    print(str1)

