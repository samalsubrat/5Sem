num = int(input("Enter a number: "))
digits = set(str(num))
digit_names = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

for d in digits:
    print(digit_names[int(d)], end=" ")
