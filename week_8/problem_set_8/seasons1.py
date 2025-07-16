# seasons.py

from datetime import date, datetime
import re
import sys

def main():
    str1 = input("Date of Birth: ")
    match = re.search(r"^(\d{4}-\d{2}-\d{2})$",str1)
    if not match :
        sys.exit("Invalid date")

    #birth_day = datetime.strptime(match.group(1), "%Y-%m-%d")
    birth_day = date.strftime(match.group(1),"%Y-%m-%d")

    now = date.today()
    delta = now - birth_day
    print("Birthday: ",birth_day)
    print("now: ",now)
    print("delta: ",delta)




if __name__ == "__main__":
    main()