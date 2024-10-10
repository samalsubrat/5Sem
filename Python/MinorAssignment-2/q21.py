n = int(input("Enter a number: "))
fact = 1
i = 1
while fact < n:
    i += 1
    fact *= i
if fact == n:
    print(f"{n} is a factorial number.")
else:
    print(f"{n} is not a factorial number.")
