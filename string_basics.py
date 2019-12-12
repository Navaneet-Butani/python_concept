s = 'Hello! How are you!'
print(s)

# Multi line string
s1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(s1)

# Strip
z = "       Hi. My name is Joe. "
print(z)
print(z.strip())

y = 'hello. how do you do?'
print("Upper : " + y.upper())
print("Lower : "+ y.lower())
print(y.capitalize())

# Split and store into the list
l = s1.split(",")
print(l)

l = s1.split(",", 1)
print(l)

l = s1.split(",", 0)
print(l)

# Count
print("No of 's' in string :", s1.count('s', 0, 10))

# Encoding
e = s.encode(encoding='big5')
print(e)
# Decoding
print(e.decode(encoding='big5'))

# Is Title
print(s.istitle())

# Join
l = ['hello!', 'Nice', 'to', 'meet you!']
print("-".join(l))

# Fill
print(s.zfill(50))

# Center
print(s.center(100, "-"))

# Concatenation
print(s+"Bye.")
print(s, 5,6,10)
print("Sum is %d and avg is %f." % (169, 5.8))
print("Sum is {} and avg is {}.".format(169, 5.8))
