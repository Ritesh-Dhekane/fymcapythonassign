# Program with 5 functions to perform operations on a Dictionary
print("Name = Ritesh Dhekane")

# 1️⃣ Function to print all keys
def print_keys(d):
    print("Keys in dictionary:")
    for key in d:
        print(key)


# 2️⃣ Function to print all values
def print_values(d):
    print("Values in dictionary:")
    for key in d:
        print(d[key])


# 3️⃣ Function to find length of dictionary
def dict_length(d):
    count = 0
    for _ in d:
        count += 1
    return count


# 4️⃣ Function to search a key
def search_key(d, key):
    if key in d:
        print("Key found! Value =", d[key])
    else:
        print("Key not found!")


# 5️⃣ Function to print sum of all values (if numeric)
def sum_of_values(d):
    total = 0
    for key in d:
        total += d[key]
    return total


# ==== Main Program ====
# Create a dictionary from user input
n = int(input("Enter number of key-value pairs: "))
d = {}

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value

print("\nDictionary entered:", d)
print_keys(d)
print_values(d)
print("Length of dictionary:", dict_length(d))

search_key(d, input("Enter key to search: "))
print("Sum of all values:", sum_of_values(d))
