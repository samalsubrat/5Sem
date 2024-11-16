def binary_to_decimal(binary):
    decimal, power = 0, 0
    while binary > 0:
        decimal += (binary % 10) * (2 ** power)
        binary //= 10
        power += 1
    return decimal

def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

# Example usage
binary_num = 1010
decimal_num = 10
print("Binary to Decimal:", binary_to_decimal(binary_num))
print("Decimal to Binary:", decimal_to_binary(decimal_num))
