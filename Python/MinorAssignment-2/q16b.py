import math

x = float(input("Enter x: "))
n = int(input("Enter number of terms (n): "))
sum_b = 1
for i in range(1, n+1):
    sum_b += (x**i) / math.factorial(i)
print("Sum of series b:", sum_b)
