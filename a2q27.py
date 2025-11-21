# 27. Python program to create a separate list of digits from a mixed list using list comprehension

print("Name = Ritesh Dhekane")

# Original list
input_list = ['a', 'b', 2, 43, 'Hi', 900, 'xyz']

# Using list comprehension to filter only numbers
output_list = [item for item in input_list if type(item) == int or type(item) == float]

# Display result
print("Input List:", input_list)
print("Output List (only digits):", output_list)
