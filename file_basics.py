# Opening the file to work on
f = open("sample.txt", "rt")

# print(f.read())
# text = f.read(20)
# print(type(text))

print(f.read(10))
print(f.read(10))

print(f.tell())  # This will tell the position of the cursor

f.seek(1, 0)    # Will move cursor to specific location
print(f.read(10))

f.close()
