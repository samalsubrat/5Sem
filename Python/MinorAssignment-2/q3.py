score = int(input("Enter your numeric score: "))
if 90 <= score <= 100:
    print("A - Excellent")
elif 80 <= score <= 89:
    print("B - Good")
elif 70 <= score <= 79:
    print("C - Average")
elif 60 <= score <= 69:
    print("D - Needs Improvement")
else:
    print("F - Failing")
