l = [5, "Hello", 10.7, 'G', 800, 0.5567]

# Print list separately
for i in l:
    print(i)

# Accessing values
print("2nd Element :", l[1])

# Slicing
for i in l[2:]:
    print(i)

# Reverse the list
print(l[::-1])

# Append
l.append("Last Element")
print(l)

# Delete list element
del l[-1]
print(l)

# Length
print("Length of the list is :", len(l))

# Membership
print("Hello" in l)
print(100 in l)

# Max
l2= [10, 8,100.67, 0.764]
print(max(l2))


# Count
l2.append(20)
l2.append(20)
l2.append(10)
print(l2.count(20))

# Insert
print(l2)
l2.insert(1,30)
print(l2)

# Sort
l2.sort()
print(l2)

# reverse
l2.reverse()
print(l2)

# remove
l2.remove(30)
print(l2)

# Pop
l2.pop()
print(l2)

# EXTEND
l.extend(l2)
print(l)

l3 = l2.copy()
print(l3)
