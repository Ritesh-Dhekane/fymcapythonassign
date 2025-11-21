# Program to check if any character occurs 5 times consecutively in a string
print("Name = Ritesh Dhekane")

# Input string of length 10
s = input("Enter a string of length 10: ")

# Check if string length is exactly 10
if len(s) != 10:
    print("Please enter exactly 10 characters!")
else:
    found = False

    # Loop through and check consecutive characters
    for i in range(len(s) - 4):
        if s[i] == s[i+1] == s[i+2] == s[i+3] == s[i+4]:
            found = True
            break

    print(found)
