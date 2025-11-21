# 17. Python program to count the number of characters in a string

# Take input from user
string = input("Enter a string: ")

# Create an empty dictionary to store counts
char_count = {}

# Loop through each character in the string
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Display the result
print("Character count dictionary:", char_count)
