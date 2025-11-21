print("Name = Ritesh Dhekane")

# User-defined Exception
class NotEligibleForDrivingLicense(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise Exception("Age cannot be negative!")

    if age < 18:
        raise NotEligibleForDrivingLicense("NotEligibleForDrivingLicense")

    print("You are eligible for a driving license.")

except NotEligibleForDrivingLicense as e:
    print(e)

except Exception as e:
    print(e)
