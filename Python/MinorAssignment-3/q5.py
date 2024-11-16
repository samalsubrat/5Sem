def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

# Example usage
number = int(input("Enter the number: "))
print("Number of digits:", count_digits(number))
# Output: 5
