# Program to find common members in two lists
print("Name = Ritesh Dhekane")

# Input first list
n1 = int(input("Enter number of elements in first list: "))
list1 = []
for i in range(n1):
    val = int(input("Enter element: "))
    list1.append(val)

# Input second list
n2 = int(input("Enter number of elements in second list: "))
list2 = []
for i in range(n2):
    val = int(input("Enter element: "))
    list2.append(val)

# Find common elements (without using built-in set operations)
common = []

for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print("First list:", list1)
print("Second list:", list2)
print("Common elements:", common)
