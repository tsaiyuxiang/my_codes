# plates.py

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    digit_found = False
    len1 = len(s)
    if (len1 > 6) or (len1 < 2):
        return False
    ii = 0
    while (ii < len1) :
        if not( s[ii].isalpha() or s[ii].isdigit() ):
            return False
        elif ii < 2 :
            if not s[ii].isalpha():
                return False
        else :
            if (not digit_found) and s[ii].isdigit():
                digit_found = True
                if s[ii]=="0" :
                    return False
            elif digit_found and s[ii].isalpha():
                return False
        ii+=1
    return True

if __name__ == "__main__":
    main()
