# 25. Python program to find all duplicates in a list

print("Name = Ritesh Dhekane")

def dups(lst):
    duplicates = []
    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

# Example list
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]

# Call the function
result = dups(numbers)

print("Duplicate elements are:", result)
