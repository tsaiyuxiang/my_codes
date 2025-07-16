# response.py
import validators

e_addr = input("What's your email address? ")
if validators.email(e_addr):
    print("Valid")
else:
    print("Invalid")


