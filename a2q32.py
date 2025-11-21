print("Name = Ritesh Dhekane")

def how_many(aDict):
    count = 0
    for value in aDict.values():
        count += len(value)
    return count

def biggest(aDict):
    largest_key = None
    largest_size = 0
    for key, value in aDict.items():
        if len(value) > largest_size:
            largest_size = len(value)
            largest_key = key
    return largest_key

# Given dictionary
animals = {
    'L': ['Lion'],
    'D': ['Donkey', 'Deer'],
    'E': ['Elephant']
}

print("Given dictionary :")
for k, v in animals.items():
    print(k, ":", v)

print("\nNumber of animals :", how_many(animals))
print("Largest :", biggest(animals))
