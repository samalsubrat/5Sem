p = 1000
r = 0.12
for n in [10, 20, 30]:
    a = p * (1 + r)**n
    print(f"Amount after {n} years: Rs. {a:.2f}")
