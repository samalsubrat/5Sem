n = int(input("Enter a positive integer: "))
reverse_num = 0
while n > 0:
    reverse_num = reverse_num * 10 + n % 10
    n //= 10
print(f"Reversed number: {reverse_num}")
