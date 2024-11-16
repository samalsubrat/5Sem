from itertools import permutations

def unique_permutations(s):
    return set(''.join(p) for p in permutations(s))

# Example usage
print(unique_permutations("abc"))
