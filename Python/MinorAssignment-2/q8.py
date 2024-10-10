while True:
    num = int(input("Enter a positive number: "))
    if num > 0:
        break

if num % 2 == 0:
    print(num * 2)
else:
    print(num ** 2)
