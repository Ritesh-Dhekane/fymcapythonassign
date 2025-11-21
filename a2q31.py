# 31. Python program to print two dictionaries based on character frequency

print("Name = Ritesh Dhekane")

# Take string input
text = input("Enter a string: ")

# Dictionary to store character frequencies
char_count = {}

for ch in text:
    char_count[ch] = char_count.get(ch, 0) + 1

# Dictionary to group characters by frequency
freq_dict = {}

for ch, count in char_count.items():
    if count in freq_dict:
        freq_dict[count].append(ch)
    else:
        freq_dict[count] = [ch]

# Print both dictionaries
print("Output 1:", char_count)
print("Output 2:", freq_dict)
