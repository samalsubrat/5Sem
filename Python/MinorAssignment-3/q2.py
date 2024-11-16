def find_numbers():
    result = [num for num in range(100, 501) if num % 3 == 0 and num % 5 == 0]
    return result

print("Numbers between 100 and 500 divisible by 3 and multiples of 5:", find_numbers())
