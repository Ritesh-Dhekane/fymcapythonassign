# Program to reverse digits of a number (works for negative numbers)
print("Name = Ritesh Dhekane")

# Input number
n = int(input("Enter a number: "))

# Check if negative
negative = False
if n < 0:
    negative = True
    n = -n   # make it positive for reversal

rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

# If original number was negative, make result negative
if negative:
    rev = -rev

print("Reversed number is:", rev)