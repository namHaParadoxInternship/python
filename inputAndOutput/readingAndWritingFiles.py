import json
# Make a write only file
f = open('workfile', 'w')

# Using 'with' to close the file right after using it
with open('workfile') as f:
    read_data = f.read()

print(f.closed)

# or close it manually
f = open('workfile', 'r')
f.close()
print(f.closed)


# Make a file with single line
with open('singleLine', 'w') as f:
    # f.write() return number of characters written
    print(f.write('This is a file with only 1 line\n'))


with open('singleLine', 'r') as f:
    print(repr(f.read()))


# Make a file with multiple lines
listOfLines = ['This is the first line\n', 'And this is the last line\n']
with open('multipleLines', 'w') as f:
    for line in listOfLines:
        f.write(line)

# read entire file
with open('multipleLines', 'r') as f:
    print(repr(f.read()))

# read single line
with open('multipleLines', 'r') as f:
    print(repr(f.readline()))
    print(repr(f.readline()))
    print(repr(f.readline()))

# loop over file object
with open('multipleLines', 'r') as f:
    for line in f:
        print(repr(line), end='\n')


# Convert a tuple to string to write into file
value = ('the answer', 42)
s = str(value)
with open('writingTuple', 'w') as f:
    f.write(s)

with open('writingTuple', 'r') as f:
    for line in f:
        print(repr(line), end='\n')


# Change file object's position
# make a blank file in case of failure read
with open('positioning', 'w') as f:
    f.write('')
f = open('positioning', 'rb+')
f.write(b'0123456789abcdef')

# go to the 6th byte in the file
f.seek(5)
print(repr(f.read(1)))

# go to the 3rd byte before the end
f.seek(-3, 2)
print(repr(f.read(1)))

f.close()


# Saving structured data with json
dict = {
    1: "nam",
    2: "tu",
    3: "linh"
}

with open('dump', 'w') as f:
    json.dump(dict, f)

with open('dump', 'r') as f:
    print(repr(json.load(f)))