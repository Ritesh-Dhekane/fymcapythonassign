print("Name = Ritesh Dhekane")

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage
numbers = [2, 4, 7, 9, 11, 15, 17]
print("List:", numbers)

result = [is_prime(n) for n in numbers]
print("Prime check result:", result)
