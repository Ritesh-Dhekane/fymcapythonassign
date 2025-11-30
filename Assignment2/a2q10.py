# Program with 5 functions to perform operations on a list
print("Name = Ritesh Dhekane")

# 1️⃣ Function to find sum of elements
def list_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total


# 2️⃣ Function to find maximum element
def list_max(lst):
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum


# 3️⃣ Function to find minimum element
def list_min(lst):
    minimum = lst[0]
    for num in lst:
        if num < minimum:
            minimum = num
    return minimum


# 4️⃣ Function to reverse a list
def reverse_list(lst):
    rev = []
    for i in range(len(lst) - 1, -1, -1):
        rev.append(lst[i])
    return rev


# 5️⃣ Function to count even numbers
def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count


# ==== Main Program ====
# Accept list elements from user
n = int(input("Enter number of elements in list: "))
lst = []

for i in range(n):
    val = int(input("Enter element: "))
    lst.append(val)

# Perform operations
print("Sum of elements:", list_sum(lst))
print("Maximum element:", list_max(lst))
print("Minimum element:", list_min(lst))
print("Reversed list:", reverse_list(lst))
print("Count of even numbers:", count_even(lst))
