# 21. Python program to sort (name, age, height) tuples

print("Name = Ritesh Dhekane")

# Take input from user
# Example input: Ritesh,22,170
data = []
while True:
    line = input("Enter name, age, height (or press Enter to stop): ")
    if not line:
        break
    name, age, height = line.split(',')
    data.append((name, int(age), int(height)))

# Sort by name, then age, then height
sorted_data = sorted(data, key=lambda x: (x[0], x[1], x[2]))

# Print sorted list
print("\nSorted data:")
for item in sorted_data:
    print(item)
