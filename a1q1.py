# Program to compute GCD of two numbers (without built-in function)
print("Name = Ritesh Dhekane")

# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Find GCD using while loop
while b != 0:
    temp = b
    b = a % b
    a = temp

print("GCD is:", a)
