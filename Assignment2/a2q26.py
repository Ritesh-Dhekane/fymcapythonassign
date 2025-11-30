# 26. Python program to add two matrices using lists

print("Name = Ritesh Dhekane")

# Accept matrix size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input first matrix
print("\nEnter elements for Matrix 1:")
matrix1 = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"Enter element [{i+1}][{j+1}]: "))
        row.append(val)
    matrix1.append(row)

# Input second matrix
print("\nEnter elements for Matrix 2:")
matrix2 = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"Enter element [{i+1}][{j+1}]: "))
        row.append(val)
    matrix2.append(row)

# Add the matrices
result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

# Display result
print("\nResultant Matrix after Addition:")
for row in result:
    print(row)
