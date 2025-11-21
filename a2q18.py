# 18. Python program to test if list contains elements in a given range

# Sample list
numbers = [15, 22, 19, 30, 25]

# Take input for range
low = int(input("Enter lower range: "))
high = int(input("Enter upper range: "))

# Check if all elements are within range
in_range = True
for num in numbers:
    if num < low or num > high:
        in_range = False
        break

# Display result
if in_range:
    print("All elements are within the range.")
else:
    print("Some elements are outside the range.")
