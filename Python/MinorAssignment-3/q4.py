def reverse_string(s):
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

# Example usage
input_string = input("Enter the string to reverse: ")
print("Reversed string:", reverse_string(input_string))
# Output: "olleh"
