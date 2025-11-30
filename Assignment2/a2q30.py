# 30. Python program to print the string with maximum length

print("Name = Ritesh Dhekane")

def max_length_string(str1, str2):
    if len(str1) > len(str2):
        print("String with maximum length:", str1)
    elif len(str2) > len(str1):
        print("String with maximum length:", str2)
    else:
        print("Both strings have the same length:")
        print(str1)
        print(str2)

# Take input from user
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Call the function
max_length_string(s1, s2)
