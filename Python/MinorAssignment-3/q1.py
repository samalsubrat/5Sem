def three_greatest_digits(number):
    digits = [int(d) for d in str(number)]
    unique_digits = sorted(set(digits), reverse=True)
    return unique_digits[:3]

number = 6328
print("The first, second, and third greatest digits are:", three_greatest_digits(number))
