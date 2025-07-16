# um.py
import re

def main():
    print(count(input("Text: ")))

def count(s):

    #pattern = r"[^[A-Z]\d]um[^[A-Z]\d]"

    # \b 代表單字邊界，um 前後不能是其他字母
    pattern = r"\bum\b"
    matches = re.findall(pattern, s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
