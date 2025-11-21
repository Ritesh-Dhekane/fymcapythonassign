# Program to find Union, Intersection, Difference and Symmetric Difference between two sets
print("Name = Ritesh Dhekane")

# Input first set
n1 = int(input("Enter number of elements in first set: "))
set1 = set()
for i in range(n1):
    val = input("Enter element: ")
    set1.add(val)

# Input second set
n2 = int(input("Enter number of elements in second set: "))
set2 = set()
for i in range(n2):
    val = input("Enter element: ")
    set2.add(val)

# Perform set operations
union_set = set1 | set2
intersection_set = set1 & set2
difference_set = set1 - set2
symmetric_diff_set = set1 ^ set2

# Display results
print("\nFirst set:", set1)
print("Second set:", set2)
print("\nUnion:", union_set)
print("Intersection:", intersection_set)
print("Difference (set1 - set2):", difference_set)
print("Symmetric Difference:", symmetric_diff_set)
