# reading mbox-short.txt and splitting email address from the text
fname = input("Enter a valid file name: ")
fh = open(fname)

count = 0
for emails in fh:
    emails = emails.rstrip() # deleting white space between each line
    if not emails.startswith('From:'):
        continue # skipping lines that don't start with "From:"
    else:
        emails = emails.split() # splitting the words in each line
    count = count + 1 # counting lines that start with From:
    print(emails[1]) # printing only the email addresses from each line

print("There are",count,"lines.")