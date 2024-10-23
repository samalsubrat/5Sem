for i in range(1, 5):
    print('*' * i)
print()
for i in range(4, 0, -1):
    print('*' * i)
print()
for i in range(4, 0, -1):
    print(' ' * (4 - i) + '*' * i)
print()
for i in range(1, 5):
    print(' ' * (4 - i) + '*' * i)
print()
for i in range(5):
    print('* ' * (i + 1))
print()
for i in range(5, 0, -1):
    print(' ' * (5 - i) + '* ' * i)
print()
for i in range(5):
    print(' ' * i + '*' * (5 - i))
print()
for i in range(6):
    for j in range(6 - i):
        print(j, end=" ")
    print()
print()
for i in range(1, 6):
    print(str(i) * i)
print()
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end="")
    print()
print()
for i in range(1, 6):
    print(i * 2, end=" ")
    for j in range(2, i + 2):
        print(i * 2 * j, end=" ")
    print()
print()
start = ord('A')
for i in range(6):
    for j in range(i):
        print(chr(start), end=" ")
        start += 1
    print()



