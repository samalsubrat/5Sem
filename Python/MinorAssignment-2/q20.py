n = int(input("Enter an integer: "))
i = 2
factors = []

while True:
    if n == 1:
        break
    elif n % i == 0:
        factors.append(i)
        n //= i
    else:
        i += 1

print("Smallest factors:", factors)
