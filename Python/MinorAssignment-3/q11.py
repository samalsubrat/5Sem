def can_form_palindrome(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    odd_count = 0
    for count in freq.values():
        if count % 2 != 0:
            odd_count += 1

    return odd_count <= 1

# Example usage
s = "civic"
print("Can form palindrome:", can_form_palindrome(s))
# Output: True
