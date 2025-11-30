# Program to print alphabet pattern
print("Name = Ritesh Dhekane")

# Number of rows
rows = 5

for i in range(rows):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")   # chr(65) = 'A'
    print()   # Move to next line
