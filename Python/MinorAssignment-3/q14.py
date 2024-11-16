def is_armstrong(number):
    sum_of_powers = 0
    temp = number
    digits = len(str(number))

    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** digits
        temp //= 10

    return sum_of_powers == number

# Example usage
num = 153
print("Is Armstrong:", is_armstrong(num))
# Output: True
