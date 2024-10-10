amount = int(input("Enter amount to withdraw: "))
if amount % 10 != 0:
    print("Amount must be a multiple of 10.")
else:
    notes = [100, 50, 20, 10]
    for note in notes:
        count = amount // note
        amount %= note
        if count > 0:
            print(f"{count} notes of {note}")
