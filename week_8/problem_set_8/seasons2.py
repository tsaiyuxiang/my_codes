# seasons.py

from datetime import date
import re
import sys
from num2words import num2words

def main():
    print(convert(input("Date of Birth: ")))

def convert(s):
    match = re.search(r"^(\d{4})-(\d{2})-(\d{2})$",s)
    if not match :
        return "Invalid date"
    y1, m1, d1 = match.groups()
    try :
        birth_day = date(int(y1), int(m1), int(d1))
    except ValueError :
        return "Invalid date"
    #now = date.today()
    now = date(2000,1,1)  # for testimg
    delta = now - birth_day
    delta_minutes = delta.days * 1440
    delta_minutes_str = num2words(delta_minutes).capitalize()+" minutes"
    delta_minutes_str = delta_minutes_str.replace(" and","")
    return delta_minutes_str

    #print(delta_minutes_str.capitalize()+" minutes")
    #print("Birthday: ",birth_day)
    #print("now: ",now)
    #print("delta: ",delta)
    #print(f"delta_minutes: {delta_minutes} {delta_minutes_str}")

if __name__ == "__main__":
    main()
