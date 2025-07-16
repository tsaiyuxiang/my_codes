# twttr.py

import re


def main():
    str1 = input("Input: ")
    print(shorten(str1))

def shorten(str1):
    return re.sub(r"[AEIOUaeiou]", "", str1)

if __name__ == "__main__":
    main()

