d = {
    'Name': "Jay",
    "College": "GEC",
    "Branch": "CE"
}

print(d)

print(d['Name'])
print(d.get('College'))

# Keys
for i in d:
    print(i)

# Values
for i in d:
    print(d[i])

for i in d.values():
    print(i)

for i in d.items():
    print(i)


for i,j in d.items():
    print(i, j)

# Add
d["City"] = "Rajkot"
print(d)

# Remove
d.pop("Branch")
print(d)

# # Clear
# d.clear()
# print(d)

# String representation
print(str(d))

d1 = {
    "Name": "Kevin",
    "Gender": "Male"
}

# Update
d.update(d1)
print(d)
