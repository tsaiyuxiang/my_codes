# coke.py
if __name__ == "__main__":
    amount_due = 50
    while amount_due > 0 :
        print(f"Amount Due: {amount_due}")
        insert_coin = int(input("Insert Coin: "))
        if (insert_coin == 25) or (insert_coin == 10) or (insert_coin == 5) :
            amount_due = amount_due - insert_coin

    if amount_due < 0 :
        amount_due = -1 * amount_due
    print(f"Change Owed: {amount_due}")
