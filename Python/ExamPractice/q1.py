import copy

original_list = [['Shallow', 2, 3], [4, 5, 6]]
shallow_copy = original_list.copy()
deep_copy = copy.deepcopy(original_list)

# Modify original list
original_list[0][0] = 'Modified'

print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)
