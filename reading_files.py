""" # reads whole file with line spaces
ofile = open('options.txt')
for of in ofile:
    print(of)
"""
''' # counts line in file
ofile = open('options.txt')
count = 0

for line in ofile:
   count = count + 1
print("Line count total: ",count)
'''
''' # prints total characters in the file
ofile = open('options.txt')
inp = ofile.read()
print(len(inp))

print(inp[:20]) # prints characters up to 20
'''
''' # if line starts with "sound" reads that line
ofile = open('options.txt')
for line in ofile:
    line = line.rstrip() # stops line spacing between each line
    if line.startswith("sound"):
        print(line)
'''
'''
# if line starts with "sound" reads that line
ofile = open('options.txt')
for line in ofile:
    line = line.rstrip()  # stops line spacing between each line
    if not "soundCategory" in line:
        continue
    print(line)
'''
# makes user input a valid available file
while True:
    fname = input("Enter a text file: ")
    try:
        fhand = open(fname)
        break
    except:
        print("File can't be found:", fname)
        print("Please enter a file")

# stops line spaces, counts lines that start with key_key.waila, and reads lines with .waila in it
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith("key_key.waila"):
        count = count + 1
    if not '.waila' in line:
        continue
    print(line)

# number of subject lines that start with key_key.waila
print("There are", count, "subject lines in", fname)

print("done")

