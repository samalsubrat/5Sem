text = input("Enter a string: ")
for i in range(len(text)):
    for j in range(i+1, len(text)+1):
        print(text[i:j])
