s = "code tantra"
print("printing the string in different ways...")
print(s)              # Prints the entire string: "code tantra"
print(s[:])           # Slices the entire string (default start and end): "code tantra"
print(s[0:])          # Slices from index 0 to the end: "code tantra"
print(s[:11])         # Slices from the start to index 11 (length of the string): "code tantra"
print(s[0:11])        # Same as above, explicitly including start and end: "code tantra"

print("Slicing....")
print(s[0:4])         # Slices from index 0 to 4 (excludes 4): "code"
print(s[5:])          # Slices from index 5 to the end: "tantra"
# s[6] = "M"          # Uncommenting this line will throw an error as strings are immutable in Python.
print(s[0:5] + "Mantra") # Concatenates sliced string and "Mantra": "code Mantra"
print(s[6:9])         # Slices from index 6 to 9: "tan"
print(s[9:6])         # Slicing in increasing order with start > end gives an empty string: ""

print("negative indexing...")
print(s[-3:-7])       # Negative indexing in decreasing order gives an empty string: ""
print(s[-6:-2])       # Slices from -6 (index 5) to -2 (index 8): "tant"

print("jump slicing...")
print(s[::2])         # Jumps every 2nd character, from start to end: "cd atra"
print(s[::-1])        # Reverses the string: "artnat edoc"
print(s[::-2])        # Reverses and skips every second character: "atntec"
