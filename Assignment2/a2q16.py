# 16. Python program to sort a dictionary by key and by value

# Sample dictionary
my_dict = {'apple': 5, 'banana': 2, 'cherry': 7, 'date': 4}

# Sort by key (ascending)
sorted_by_key_asc = dict(sorted(my_dict.items()))
print("Sorted by key (ascending):", sorted_by_key_asc)

# Sort by key (descending)
sorted_by_key_desc = dict(sorted(my_dict.items(), reverse=True))
print("Sorted by key (descending):", sorted_by_key_desc)

# Sort by value (ascending)
sorted_by_value_asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print("Sorted by value (ascending):", sorted_by_value_asc)

# Sort by value (descending)
sorted_by_value_desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print("Sorted by value (descending):", sorted_by_value_desc)
