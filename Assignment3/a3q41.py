print("Name = Ritesh Dhekane")


def is_valid_password(password):
    if len(password) < 6 or len(password) > 16:
        return False

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for ch in password:
        if ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        elif ch in "$#@":
            has_special = True

    return has_lower and has_upper and has_digit and has_special


# Taking input from user
pwd = input("Enter password: ")

if is_valid_password(pwd):
    print("Valid Password")
else:
    print("Invalid Password")
