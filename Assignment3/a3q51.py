print("Name = Ritesh Dhekane")

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

try:
    n = int(input("Enter a number: "))

    if n < 0:
        raise Exception("Negative numbers cannot be checked for prime!")

    if is_prime(n):
        print(n, "is a Prime Number")
    else:
        print(n, "is NOT a Prime Number")

except ValueError:
    print("Invalid input! Please enter an integer.")

except Exception as e:
    print(e)
