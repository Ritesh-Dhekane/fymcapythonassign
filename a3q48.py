import threading

print("Name = Ritesh Dhekane")

# Create RLock object
lock = threading.RLock()

def factorial(n, label):
    lock.acquire()
    try:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        print(f"Factorial of {label} ({n}) = {fact}")
    finally:
        lock.release()

# Accept inputs
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Create threads
t1 = threading.Thread(target=factorial, args=(num1, "Number 1"))
t2 = threading.Thread(target=factorial, args=(num2, "Number 2"))

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("Both factorial calculations completed.")
