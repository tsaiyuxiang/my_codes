# fuel.py

def main():
    while True:
        str1 = input("Fraction: ")
        try:
            v = convert(str1)
            break
        except (ValueError, ZeroDivisionError):
            continue
    print(gauge(v))


def convert(fraction):
    if "/" not in fraction:
        raise ValueError("Missing '/'")

    x_str, y_str = fraction.split("/", 1)

    try:
        x = int(x_str)
        y = int(y_str)
    except ValueError:
        raise ValueError("Non-integer input")

    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")

    if x < 0 or y < 0 or x > y:
        raise ValueError("Invalid fraction range")

    return round(x / y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()


'''
def main():
    while True:
        str1 = input("Fraction: ")
        try :
            v = convert(str1)
            break
        except ValueError :
            continue
        except ZeroDivisionError :
            continue
    print(gauge(v))

def convert(fraction):
    if fraction.count("/") == 1:
        fraction_split = fraction.split("/", 1)
        try:
            x = int(fraction_split[0])
            y = int(fraction_split[1])
        except ValueError:
            raise
        if y == 0 :
            raise ZeroDivisionError("ZeroDivisionError")
        if x < 0 or y < 0:
            raise ValueError("ValueError")
        elif x > y :
            raise ValueError("ValueError")
        v = round(float(x / y) * 100.0)
    else :
        raise ValueError("ValueError")
    return v

def gauge(percentage):
    if percentage <= 1:
        return("E")
    elif percentage >= 99:
        return("F")
    else:
        return(f"{percentage}%")

if __name__ == "__main__":
    main()
'''
