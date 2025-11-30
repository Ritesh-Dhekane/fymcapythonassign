# Program to find factorial of a number
print("Name = Ritesh Dhekane")

# Input number
n = int(input("Enter a number: "))

fact = 1

# Multiply numbers from 1 to n
for i in range(1, n + 1):
    fact = fact * i

print("Factorial of", n, "is:", fact)
