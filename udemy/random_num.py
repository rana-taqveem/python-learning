import random


for i in range(1, 10):
    print(f'i: {i}')
    num = random.randrange(1, 2)  # Generates a random integer between 1 and 10 (inclusive)
    print(f"Random integer between 1 and 10: {num}")


for i in range(0, 50):
    num = random.uniform(1,2)
    print(f"Random float between 1 and 2: {num}")

    