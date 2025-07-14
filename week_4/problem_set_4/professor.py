# professor.py 2025/07/09

import random

def main() :
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        j = 0
        while True:
            print(f"{x} + {y} = ", end="")
            try:
                j += 1
                z = int(input(""))  # answer
            except EOFError:
                exit(0)
            except ValueError:
                if j >= 3:
                    print(f"{x} + {y} = {x+y}")
                    break
                else:
                    print("EEE")
                    continue
            if x + y == z:
                score += 1
                break
            else:
                if j >= 3:
                    print(f"{x} + {y} = {x+y}")
                    break
                else:
                    print("EEE")
                continue
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 3 or level < 1:
                continue
            else:
                break
        except ValueError:
            continue
        except EOFError:
            exit(0)
    return level

def generate_integer(level):
    match level:
        case 1:
            v = random.randint(0, 9)
        case 2:
            v = random.randint(10, 99)
        case 3:
            v = random.randint(100, 999)
        case _ :
            raise ValueError
    return v

if __name__ == "__main__":
    main()



