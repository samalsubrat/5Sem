def sum_even_squares():
    total = 0
    for i in range(1, 51):
        if i % 2 == 0:
            total += i * i
    return total

# Example usage
print("Sum of squares of even numbers between 1 and 50:", sum_even_squares())
