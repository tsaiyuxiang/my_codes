# taqueria 2025/07/06

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0
order=[]
while True:
    try :
        item = input("Item: ")
        item = item.title()
        if item in menu:
            order.append(item)
            total += menu[item]
            print(f"Total: ${total:.2f}")
    except EOFError:
        print(f"Order: {order}")
        break

