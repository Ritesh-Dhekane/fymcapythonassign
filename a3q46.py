print("Name = Ritesh Dhekane")

try:
    age = int(input("Enter your age: "))

    # Check for negative age
    if age < 0:
        raise Exception("Invalid age! Age cannot be negative.")

    # Check voting eligibility
    if age < 18:
        raise Exception("Not eligible for voting. Must be 18 or above.")
    
    print("You are eligible to vote.")

except Exception as e:
    print(e)
