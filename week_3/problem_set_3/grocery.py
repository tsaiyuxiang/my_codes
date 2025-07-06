# grocery.py 2025/07/06

grocery = {}
while True:
    try :
        item = input("")
    except EOFError:
        break
    item = item.upper()
    if grocery.get(item) == None:
        grocery[item] = 1
    else:
        grocery[item] += 1
#print(f"B4: {grocery}")
grocery_key_sorted = sorted(grocery)
#print(f"AF: {grocery_key_sorted}")
for i in grocery_key_sorted:
    print(f"{grocery.get(i)} {i}")
