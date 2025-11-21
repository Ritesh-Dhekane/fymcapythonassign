print("Name = Ritesh Dhekane")

try:
    password = input("Enter your password: ")

    # Check password length (you can modify the limits)
    if len(password) < 6 or len(password) > 12:
        raise Exception("Invalid Password Length! Password must be between 6 and 12 characters.")

    print("Password length is valid.")

except Exception as e:
    print(e)
