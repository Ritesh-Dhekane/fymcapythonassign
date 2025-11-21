# 29. Python program to reverse a list without using reverse() function

print("Name = Ritesh Dhekane")

def reverse(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

# Example list
numbers = [10, 20, 30, 40, 50]

# Call the function
result = reverse(numbers)

print("Original List:", numbers)
print("Reversed List:", result)
