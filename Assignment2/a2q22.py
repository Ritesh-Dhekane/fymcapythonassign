# 22. Python program to compute frequency of words and store in dictionary

print("Name = Ritesh Dhekane")

# Take input from user
text = input("Enter a line of text: ")

# Split text into words
words = text.split()

# Create dictionary to count frequency
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Sort dictionary by key (alphabetically)
sorted_freq = dict(sorted(word_freq.items()))

# Print the sorted dictionary
print("\nWord frequency (sorted by word):")
print(sorted_freq)
