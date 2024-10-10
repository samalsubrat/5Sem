import math

x = float(input("Enter x: "))
n = int(input("Enter number of terms (n): "))
sum_a = 0
for i in range(n+1):
    term = (-1)**i * (x**(2*i)) / math.factorial(2*i)
    sum_a += term
print("Sum of series a:", sum_a)
