# Program with 5 functions to perform operations on strings
print("Name = Ritesh Dhekane")

# 1️⃣ Function to find length of string
def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count


# 2️⃣ Function to reverse a string
def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev


# 3️⃣ Function to count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


# 4️⃣ Function to check if string is palindrome
def is_palindrome(s):
    return s == reverse_string(s)


# 5️⃣ Function to count number of words in a string
def count_words(s):
    words = 1
    for ch in s:
        if ch == " ":
            words += 1
    return words


# ==== Main Program ====
text = input("Enter a string: ")

print("Length of string:", string_length(text))
print("Reversed string:", reverse_string(text))
print("Number of vowels:", count_vowels(text))
print("Is palindrome?:", is_palindrome(text))
print("Number of words:", count_words(text))
