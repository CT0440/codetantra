# All Dictionary Operations in Python

# Creating dictionaries
d1 = {"name": "Alice", "age": 25, "city": "New York"}  # Regular dictionary
d2 = dict(a=1, b=2, c=3)  # Using dict constructor
d3 = dict([("x", 10), ("y", 20)])  # From list of tuples
print("Dictionaries:", d1, d2, d3)  # Output: Dictionary examples

# Accessing values
print(d1["name"])  # Output: Alice
print(d1.get("city", "Not Found"))  # Output: New York
print(d1.get("country", "Not Found"))  # Output: Not Found

# Adding and updating elements
d1["country"] = "USA"  # Adding new key-value pair
d1["age"] = 30  # Updating existing value
d1.update({"profession": "Engineer", "hobby": "Reading"})  # Multiple updates
print("Updated dictionary:", d1)  # Output: Updated dictionary

# Removing elements
print("Popped value:", d1.pop("hobby"))  # Output: Reading
d1.popitem()  # Removes the last inserted pair (profession)
del d1["city"]  # Deletes key 'city'
print("After deletions:", d1)  # Output: Dictionary after deletions
d1.clear()  # Empties the dictionary
print("Cleared dictionary:", d1)  # Output: {}

# Iterating through a dictionary
d4 = {"a": 1, "b": 2, "c": 3}
print("Keys:", [key for key in d4])  # Output: ['a', 'b', 'c']
print("Values:", [value for value in d4.values()])  # Output: [1, 2, 3]
print("Items:", [(key, value) for key, value in d4.items()])  # Output: [('a', 1), ('b', 2), ('c', 3)]

# Dictionary methods
keys = d4.keys()  # Returns dict_keys(['a', 'b', 'c'])
values = d4.values()  # Returns dict_values([1, 2, 3])
items = d4.items()  # Returns dict_items([('a', 1), ('b', 2), ('c', 3)])
d5 = d4.copy()  # Creates a shallow copy
fromkeys_dict = dict.fromkeys(["key1", "key2"], 0)  # Creates dictionary with default value 0
print("Keys, Values, Items, Copy, FromKeys:", keys, values, items, d5, fromkeys_dict)

# Dictionary comprehensions
squares = {x: x**2 for x in range(5)}  # Squares of numbers from 0 to 4
filtered = {k: v for k, v in d4.items() if v % 2 == 0}  # Filters even values
print("Dictionary Comprehensions:", squares, filtered)  # Output: Dictionary comprehensions
