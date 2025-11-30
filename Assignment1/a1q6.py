# Program to count digits in a number (works for negative numbers also)
print("Name = Ritesh Dhekane")

# Input number
n = int(input("Enter a number: "))

# If number is negative, make it positive
if n < 0:
    n = -n

count = 0

# Special case: if number is 0
if n == 0:
    count = 1
else:
    while n > 0:
        count += 1
        n //= 10

print("Number of digits is:", count)
