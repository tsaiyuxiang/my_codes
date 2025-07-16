import sys
import re
from datetime import datetime, date
from num2words import num2words

def main():
    print(convert(input("Date of Birth: ")))

def convert(dob_str):
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", dob_str):
        return "Invalid date"
    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
    except ValueError :
        return "Invalid date"
    today = date.today()

    if dob > today:
        return "Invalid date"

    diff = today - dob
    minutes = diff.days * 24 * 60

    # num2words handles commas automatically with to='cardinal'
    minutes_words = num2words(minutes, to='cardinal', lang='en')
    minutes_words = minutes_words.replace(" and ", " ")  # Ensure no "and"
    #minutes_words = minutes_words.replace("-", " ")      # Remove hyphens like "twenty-one"
    minutes_words = minutes_words.capitalize()

    return f"{minutes_words} minutes"

if __name__ == "__main__":
    main()
