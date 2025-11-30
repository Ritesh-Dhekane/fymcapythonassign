print("Name = Ritesh Dhekane")


import re

def is_valid_mobile(number):
    pattern = r'^[789][0-9]{9}$'
    if re.match(pattern, number):
        return True
    return False

mobile = input("Enter mobile number: ")

if is_valid_mobile(mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
