for i in range(100, 1001):
    if i % 5 == 0 or i % 6 == 0:
        print(i, end=' ')
        if i % 10 == 0:
            print()
