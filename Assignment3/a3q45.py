
# Print your name
print("Name = Ritesh Dhekane")

# Predefined list of employees
employees = ["Ritesh", "Amit", "Sneha", "Kiran", "Pooja"]

try:
    name = input("Enter employee name: ")

    if name not in employees:
        raise Exception("Error: Employee not found in the list!")
    else:
        print("Employee found:", name)

except Exception as e:
    print(e)
