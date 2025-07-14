# adieu.py 2025/07/09

name = list()
while True:
    try :
        name.append(input("Name: "))
    except EOFError:
        break
name_count = len(name)
if name_count < 1 :
    exit(1)
print("Adieu, adieu, to", end = "")
for i in range(name_count):
    if i == 0 :
        print(" " + name[i], end = "")
    elif (i == 1) and ( i == name_count -1) :  # the last one
        print(" and " + name[i], end = "")
    elif i == name_count - 1:   # the last one
        print(", and " + name[i], end="")
    else:
        print(", " + name[i], end = "")
print("")
