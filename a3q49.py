import threading
import time

print("Name = Ritesh Dhekane")

# Function to print square
def print_square(n):
    sq = n * n
    print(f"Square of {n} = {sq}")

# Function to print factorial
def print_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"Factorial of {n} = {fact}")

# Input from user
num = int(input("Enter a number: "))

# Start time
start = time.time()

# Create threads
t1 = threading.Thread(target=print_square, args=(num,))
t2 = threading.Thread(target=print_factorial, args=(num,))

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

# End time
end = time.time()

print(f"Total time taken: {end - start} seconds")
