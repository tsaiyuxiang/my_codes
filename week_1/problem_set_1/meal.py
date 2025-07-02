# meal.py 2025/07/01
def main() :
    time = input("What time is it? ")
    time_value = convert(time)
    ans = ""
    if (time_value >= 7.0) and (time_value <= 8.0) :
        ans = "breakfast time"
    elif (time_value >= 12.0) and (time_value <= 13.0) :
        ans = "lunch time"
    elif (time_value >= 18.0) and (time_value <= 19.0) :
        ans = "dinner time"
    if ans != "" :
        print(ans)

def convert(time) :
    hour, minute = time.split(":",1)
    hour = float(hour)
    minute = float(minute) / 60
    time_val = hour+minute
#    print(f"The time is: {time_val}")
    return time_val

if __name__ == "__main__":
  main()
