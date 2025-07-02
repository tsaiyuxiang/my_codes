# deep.py 2025/07/01
question1 = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
question1 = question1.strip().lower()
answer = "No"
if question1 == "42" or question1 == "forty-two" or question1 == "forty two":
    answer = "Yes"
print(answer)
