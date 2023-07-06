# reading mbox-short.txt email lines and printing and pulling out the time each email was sent
fh = None  # creates an empty value to stop yellow caution error
while True:  # infinite loop until file is found
    fname = input("Enter the file name: ")
    try:
        fh = open(fname)
    except:  # loops to the top of while loop if file can't be found
        print("File not found.")
        continue
    break

count = dict()
for lines in fh:
    emails = lines.rstrip()
    if not emails.startswith('From'):  # skips lines that don't start with 'From'
        continue
    emails = lines.split()  # divides each word into a list
    if len(emails) < 3:  # skips reading lines if the length is < 3
        continue
    else:
        time = emails[5]  # using the 5th index slot to get the time (Ex: 09:14:16)
        colon = time.find(':')  # finding colon in time
        hour = time[:colon]  # indexing up to but not including the colon to slice the hour from the time
        count[hour] = count.get(hour, 0) + 1  # counting the total of each hour an email has been sent within an hour

lst = list()
for k, v in count.items():  # making each hour the key and total emails sent within an hour the values
    lst.append((k, v)) # adding the keys and values to an empty list to be sorted

lst.sort()
for k, v in lst: # for the keys and values in lst, printing the keys and values
    print(k, v)

print("\nDone!")
