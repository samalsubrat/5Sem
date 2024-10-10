n = int(input("Enter a number: "))
while n >= 10:
    n = sum(int(digit) for digit in str(n))
print(f"Single-digit sum: {n}")
