column_mapping = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4,
    'e': 5, 'f': 6, 'g': 7, 'h': 8
}

position = input("Enter a position (e.g., a1, d4): ").lower()

column = position[0] 
row = int(position[1])

column_value = column_mapping.get(column, 0)

if column_value == 0 or row < 1 or row > 8:
    print("Invalid input")
else:
    if (column_value + row) % 2 == 0:
        print("The color of the square is black.")
    else:
        print("The color of the square is white.")
