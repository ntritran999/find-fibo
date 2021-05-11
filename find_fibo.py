import math

def perfect_square(n):
    return math.sqrt(n)**2==n

def is_fibonacci(m):
    return f"{m} is fibonacci number" if perfect_square(5*m*m+4) or perfect_square(5*m*m-4) else f"{m} is not fibonacci number"

# Execution code:
print(is_fibonacci(2))
