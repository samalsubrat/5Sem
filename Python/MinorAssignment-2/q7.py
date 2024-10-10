limit = int(input("Enter the limit: "))
prime_sum = 0

for num in range(2, limit):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        prime_sum += num

print(f"The sum of all prime numbers less than {limit} is {prime_sum}")
