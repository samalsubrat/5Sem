def is_palindrome(s):
    t = s.lower()
    length = len(t)
    for i in range(length // 2):
        if t[i] != t[length - i - 1]:
            return False
    return True

word = input("Enter the string: ")
print("Is palindrome:", is_palindrome(word))
