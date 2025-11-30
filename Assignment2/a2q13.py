# Program to multiply and sum all items in a list
print("Name = Ritesh Dhekane")

# Input list size
n = int(input("Enter number of elements in list: "))
lst = []

# Take list elements from user
for i in range(n):
    val = int(input("Enter element: "))
    lst.append(val)

# Initialize sum and product
total_sum = 0
total_product = 1

# Calculate sum and product
for num in lst:
    total_sum += num
    total_product *= num

# Display results
print("List entered:", lst)
print("Sum of all elements:", total_sum)
print("Product of all elements:", total_product)
