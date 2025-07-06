# outdated.py 2022/07/06

month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main() :
    while True:
        try :
            str1 = input("Date: ")
        except EOFError: # ctrl-D
            return
        if str1.count("/") ==2 :  # "6/21/2015"
            str1_split = str1.split("/",2)
            try :
                mm = int(str1_split[0])
                dd = int(str1_split[1])
                yy = int(str1_split[2])
            except ValueError :
                continue
            else:
                if (dd >= 1) and (dd <= 31) and (mm >= 1) and (mm <= 12) and (yy <= 9999) :
                    break # correct
                else :
                    continue
        elif str1.count(",") == 1 :  # "September 8, 2025"
            str1_split = str1.split(",")
            mm_dd_split = str1_split[0].split(" ") # 拆出 September 與 8
            len1 = len(mm_dd_split)
            if len1 == 2 :
                if mm_dd_split[0] in month_list :
                    mm = month_list.index(mm_dd_split[0]) + 1  # month found get 1 ~ 12
                else :
                    continue
                try :
                    dd = int(mm_dd_split[1])
                    yy = int(str1_split[1])
                    if (dd >= 1) and (dd <= 31) and (mm >= 1) and (mm <= 12) and (yy <= 9999) :
                        break # correct
                    else :
                        continue
                except ValueError :
                    continue
                else :  # correct
                    break;
            else :
                continue
        else :
            continue
    print(f"{yy:04d}-{mm:02d}-{dd:02d}")

if __name__ == "__main__":
    main()
