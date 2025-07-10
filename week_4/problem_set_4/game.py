# game.py 2025/07/09
import random

while True :
    try :
        level = int(input("Level: "))
        if level < 1 :
            continue
        else :
            break
    except ValueError :
        continue
    except EOFError :
        exit(0)

random_value = random.randint(1,level)
while True:
    try:
        guess_value = int(input("Guess: "))
        if guess_value < 0 :
            continue
    except ValueError :
        continue
    except EOFError :
        exit(0)
    if guess_value == random_value :
        print("Just right!")
        break
    elif guess_value > random_value :
        print("Too large!")
        continue
    elif guess_value < random_value :
        print("Too small!")



