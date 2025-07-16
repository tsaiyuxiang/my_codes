# numb3rs.py

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if ip.count(".") != 3 :
        return False
    for item in ip.strip().split("."):
        if item.isdigit():
            if len(item) > 2 and item[0:1] == "0":
                return False
            num = int(item)
            if num < 0 or num > 255:
                return False
        else:
            return False
    return True

if __name__ == "__main__":
    main()

