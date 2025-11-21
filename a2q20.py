# 20. Python program to generate a dictionary of (i, i*i)

print("Name = Ritesh Dhekane")

# Take input from user
n = int(input("Enter an integer number: "))

# Create an empty dictionary
square_dict = {}

# Generate dictionary with (i, i*i)
for i in range(1, n + 1):
    square_dict[i] = i * i

# Print the dictionary
print(square_dict)
