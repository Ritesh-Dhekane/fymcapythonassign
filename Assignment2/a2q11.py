# Program with 5 functions to perform operations on a Tuple
print("Name = Ritesh Dhekane")

# 1️⃣ Function to find length of tuple
def tuple_length(t):
    count = 0
    for _ in t:
        count += 1
    return count


# 2️⃣ Function to find sum of elements (assuming numeric tuple)
def tuple_sum(t):
    total = 0
    for num in t:
        total += num
    return total


# 3️⃣ Function to find maximum element
def tuple_max(t):
    maximum = t[0]
    for num in t:
        if num > maximum:
            maximum = num
    return maximum


# 4️⃣ Function to find minimum element
def tuple_min(t):
    minimum = t[0]
    for num in t:
        if num < minimum:
            minimum = num
    return minimum


# 5️⃣ Function to count even numbers (for numeric tuple)
def count_even(t):
    count = 0
    for num in t:
        if num % 2 == 0:
            count += 1
    return count


# ==== Main Program ====
# Accept tuple elements from user
n = int(input("Enter number of elements in tuple: "))
temp_list = []

for i in range(n):
    val = int(input("Enter element: "))
    temp_list.append(val)

t = tuple(temp_list)

# Perform operations
print("Tuple entered:", t)
print("Length of tuple:", tuple_length(t))
print("Sum of elements:", tuple_sum(t))
print("Maximum element:", tuple_max(t))
print("Minimum element:", tuple_min(t))
print("Count of even numbers:", count_even(t))
