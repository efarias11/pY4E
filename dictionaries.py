# reading mbox-short.txt and creating a dictionary to see which email address has sent the most emails
fname = input("Enter the file: ")
fh = open(fname)

dicts = {} # creates an empty dictionary to assign key names assigned with values
for line in fh:
    line = line.rstrip()
    if not line.startswith('From:'): # skips lines that don't start with 'From:'
        continue
    emails = line.split() # splits each word into separate indexes creating an index #
    for e_number in emails[1:]: # reads index 1 and after, skips index 0 ('From:')
        dicts[e_number] = dicts.get(e_number,0) + 1 # counts all emails and adds 1 for each other email that exists

l_count = None # creating an empty value to print the largest recurrent email number
l_email = None # creating an empty value to print the largest recurrent email address
# for every counted email and # of recurrence looking at their key(email address) and values (counted emails)
for e_number, count in dicts.items():
    if l_count is None or count > l_count: # if largest count has no value or is > count
        l_count = count
        l_email = e_number
print("Giving the email address that's sent the most emails")
print("Email address:",l_email,"\nnumber of emails sent:",l_count)