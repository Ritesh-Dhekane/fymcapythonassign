# Program to print all prime numbers from 3 to 1000
print("Name = Ritesh Dhekane")

# Loop through numbers from 3 to 1000
for num in range(3, 1001):
    is_prime = True   # Assume the number is prime
    
    # Check divisibility
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    # If number is prime, print it
    if is_prime:
        print(num, end=" ")
