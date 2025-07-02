# faces.py 2025/06/25
def convert(str1) :
    str1 = str1.replace(":)" , "🙂")
    str1 = str1.replace(":(" , "🙁")
    return str1

def main() :
    str1 = input("")
    str1 = convert(str1)
    print(str1)

main()

