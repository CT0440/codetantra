# 1. Creating a List
a = [1, 2, 3]
print(a)  # Output: [1, 2, 3]

# 2. Accessing Elements
print(a[1])  # Output: 2

# 3. Appending an Element
a.append(4)
print(a)  # Output: [1, 2, 3, 4]

# 4. Inserting an Element
a.insert(1, 5)
print(a)  # Output: [1, 5, 2, 3, 4]

# 5. Extending a List
a.extend([6, 7])
print(a)  # Output: [1, 5, 2, 3, 4, 6, 7]

# 6. Removing an Element by Value
a.remove(3)
print(a)  # Output: [1, 5, 2, 4, 6, 7]

# 7. Popping an Element by Index
popped_value = a.pop(2)
print(popped_value)  # Output: 2
print(a)  # Output: [1, 5, 4, 6, 7]

# 8. Deleting an Element by Index
del a[0]
print(a)  # Output: [5, 4, 6, 7]

# 9. Slicing a List
print(a[1:3])  # Output: [4, 6]

# 10. Finding the Index of an Element
print(a.index(6))  # Output: 2

# 11. Counting Occurrences of an Element
print(a.count(7))  # Output: 1

# 12. Sorting the List
a.sort()
print(a)  # Output: [4, 5, 6, 7]
