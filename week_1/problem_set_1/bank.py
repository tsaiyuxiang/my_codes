'''
bank.py 2025/07/01
In a file called bank.py, implement a program that prompts the user for a greeting.
If the greeting starts with “hello”, output $0. If the greeting starts with an “h”
(but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
'''

greeting = input("input a greeting: ")
greeting = greeting.strip().lower()
if greeting == "hello":
    reward = 0
elif greeting[0] == "h":
    reward = 20
else:
    reward = 100
print(f"${reward}")