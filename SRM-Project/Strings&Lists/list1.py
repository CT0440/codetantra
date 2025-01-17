#creating list
l = ["a", "apple", 30.9, 10, (10, 20, 30)]
print(l)
#using list constructer
l2 = list((1, 2, 3, "apple"))
print(l2)

#accessing list elements
a = [10, 20, 30, 40, 50]
print(a[0:3])

#adding element in to the list
b = []
b.append(10)
print(b)
b.insert(0, "hi")
print(b)
b.extend([15, 30,78])
print(b)