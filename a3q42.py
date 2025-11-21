print("Name = Ritesh Dhekane")

import re


def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    return False


email = input("Enter Email ID: ")

if is_valid_email(email):
    print("Valid Email ID")
else:
    print("Invalid Email ID")
