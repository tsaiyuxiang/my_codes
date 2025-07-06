# fuel.py 2025/07/06

while True:
    str1 = input("Fraction: ")
    if str1.count("/") == 1:
        str1_split = str1.split("/",1)
        try:
            x = int(str1_split[0])
            y = int(str1_split[1])
            if (x > y) or (x < 0) :
                continue
            v = round(float(x/y) * 100.0)
            break
        except ValueError:
            continue
        except ZeroDivisionError:
            continue

if v <= 1:
    print("E")
elif v >= 99:
    print("F")
else:
    print(f"{v}%")


