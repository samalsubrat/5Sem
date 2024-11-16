def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Example usage
n = 7
print(f"The {n}th Fibonacci number:", fibonacci(n))
# Output: 13
