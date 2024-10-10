n = int(input("Enter a number: "))
divisors_sum = 0
for i in range(1, n):
    if n % i == 0:
        divisors_sum += i
if divisors_sum == n:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")
