# seasons.py
from datetime import timedelta, date
import inflect
import sys

def main():
    print(convert(input("Date of Birth: ")))

def convert(x):
    bb = inflect.engine()
    if x.count("-") != 2 :
        sys.exit(1)
    try:
        y1, m1, d1 = x.split("-")
        yy = int(y1)
        mm = int(m1)
        dd = int(d1)
        birth = date(yy, mm, dd)
        today = date.today()
        delta = today - birth
        min = round( delta.total_seconds() / 60)
        words = bb.number_to_words(min, andword="").capitalize() + " minutes"
        return words
    except ValueError:
        return "Invalid date"
    except _ :
        return "Invalid date"

if __name__ == "__main__":
    main()
