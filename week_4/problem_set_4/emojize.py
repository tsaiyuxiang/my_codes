# emojize.py 2025/07/07

import emoji

str = input("Input: ")
print(f"Output: ", end="")
first_found = False
start_index = 0
while True:

    if not first_found:
        index = str.find(":",start_index )
        if index == -1:
            print(f"{str[start_index:]}", end="")
            break
        else :
            first_index = index
            first_found = True
            if first_index > start_index:
                print(f"{str[start_index:first_index]}", end="")

    second_index = str.find(":", first_index+1)
    if second_index == -1:
        print(f"{str[first_index:]}", end="")
        break
    else :
        em_str = str[first_index:second_index+1]
        em = emoji.emojize(em_str, language='alias')
        print(f"{em}", end="")
        first_found = False
        start_index = second_index+1

print("")


