print("Name = Ritesh Dhekane")

def compute():
    try:
        result = 5 / 0
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")

compute()
