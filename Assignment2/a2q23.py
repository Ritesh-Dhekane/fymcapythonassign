# 23. Python program to find a pair of elements (indices) whose sum equals a target number

print("Name = Ritesh Dhekane")

# Given list and target
numbers = [10, 20, 10, 40, 50, 60, 70]
target = 50

# Find indices of two numbers whose sum equals target
found = False
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print("Output:", i + 1, ",", j + 1)
            found = True
            break
    if found:
        break

if not found:
    print("No such pair found.")
