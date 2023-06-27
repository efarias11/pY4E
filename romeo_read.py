# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using
# the split() method. The program should build a list of words. For each word on each line check to see if the
# word is already in the list and if not append it to the list. When the program completes, sort and print the
# resulting words in python sort() order as shown in the desired output.
"""
fname = input("Enter file name: ")
fh = open(fname)
lst = list()  # building list from scratch saying make an empty list named lst
for line in fh:  # first for statement where i'm gonna do stripping and splitting in next two lines
    line.rstrip()
    words = line.split()
    # print (words) #checking to make sure I got all words
    for w in words:  # second for needs to be indented.I have to learn this...keeps confusing me..w, can be anything.
        if w not in lst:  # these next two lines are how the words get from "words" from line 13 into
            lst.append(w)
            # "lst" the list that was created empty. If word not in the list, it would be added or appended
        else:
            pass
lst.sort()  # this is going to sort the list  creating the order as per assignment
print(lst)  # this is where I'm gonna print or display list on screen
"""
fname = input("Please enter a valid file name: ")
fh = open(fname)

lst = list()
for line in fh:
    words = line.split()
    # print(words)
    for w in words:
        if w not in lst:
            lst.append(w)
        else:
            pass
lst.sort()
print(lst)