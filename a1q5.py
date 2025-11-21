# Program to find numbers divisible by 7 but not multiple of 5 between 2000 and 3200
print("Name = Ritesh Dhekane")

for num in range(2000, 3201):   # both included
    if (num % 7 == 0) and (num % 5 != 0):
        print(num, end=" ")
