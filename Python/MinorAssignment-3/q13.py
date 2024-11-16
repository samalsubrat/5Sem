def roman_to_integer(roman):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total, prev = 0, 0
    for char in reversed(roman):
        value = roman_map[char]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value
    return total

roman = input("Enter the number in Roman: ")
print(roman_to_integer(roman))  # Output: 9
