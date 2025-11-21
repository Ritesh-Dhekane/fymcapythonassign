# 19. Python Program to print all Possible Combinations of elements 
# in list from the two and three Digits and store both lists in dictionary

print("Name = Ritesh Dhekane")

# Sample list
numbers = [1, 2, 3, 4]

# Empty lists to store combinations
two_digit_combinations = []
three_digit_combinations = []

# Generate 2-digit combinations
for i in numbers:
    for j in numbers:
        if i != j:
            two_digit_combinations.append(int(str(i) + str(j)))

# Generate 3-digit combinations
for i in numbers:
    for j in numbers:
        for k in numbers:
            if i != j and j != k and i != k:
                three_digit_combinations.append(int(str(i) + str(j) + str(k)))

# Store both lists in a dictionary
combinations_dict = {
    "TwoDigit": two_digit_combinations,
    "ThreeDigit": three_digit_combinations
}

# Print results
print("Two-digit combinations:", combinations_dict["TwoDigit"])
print("Three-digit combinations:", combinations_dict["ThreeDigit"])
