# 1. Creating tuples
empty_tuple = ()  # Empty tuple
single_element_tuple = (1,)  # Tuple with one element (comma is mandatory)
multi_element_tuple = (1, 2, 3, 4, 5)  # Tuple with multiple elements
mixed_tuple = (1, "hello", 3.14)  # Mixed data types
print(multi_element_tuple)  # Output: (1, 2, 3, 4, 5)

# 2. Accessing elements
print(multi_element_tuple[0])  # Output: 1 (indexing)
print(multi_element_tuple[-1])  # Output: 5 (negative indexing)

# 3. Slicing
print(multi_element_tuple[1:4])  # Output: (2, 3, 4)
print(multi_element_tuple[:3])  # Output: (1, 2, 3)

# 4. Tuple concatenation
t1 = (1, 2, 3)
t2 = (4, 5)
print(t1 + t2)  # Output: (1, 2, 3, 4, 5)

# 5. Repetition
print(t1 * 2)  # Output: (1, 2, 3, 1, 2, 3)

# 6. Membership testing
print(2 in t1)  # Output: True
print(5 in t1)  # Output: False

# 7. Tuple methods
t = (1, 2, 2, 3, 4)
print(t.count(2))  # Output: 2 (occurrences of 2)
print(t.index(3))  # Output: 3 (first occurrence of 3)

# 8. Length of tuple
print(len(t))  # Output: 5

# 9. Iteration
for item in t:
    print(item)  # Output: 1 2 2 3 4

# 10. Nesting
nested_tuple = (1, (2, 3), (4, (5, 6)))
print(nested_tuple[1])  # Output: (2, 3)
print(nested_tuple[2][1])  # Output: (5, 6)

# 11. Unpacking
a, b, c = (10, 20, 30)
print(a, b, c)  # Output: 10 20 30

# 12. Immutable nature
immutable_tuple = (1, [2, 3])
# immutable_tuple[0] = 100  # Error: TypeError: 'tuple' object does not support item assignment
immutable_tuple[1][0] = 100  # Modifying mutable element inside the tuple
print(immutable_tuple)  # Output: (1, [100, 3])

# 13. Deleting a tuple
del t1
# print(t1)  # Error: NameError: name 't1' is not defined

# 14. Conversion
lst = [1, 2, 3]
converted_tuple = tuple(lst)
print(converted_tuple)  # Output: (1, 2, 3)
