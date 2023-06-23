# reading the mbox-short.txt and extracting floating values from lines read to average the total
fname = input("Enter the file name: ")
fhandel = open(fname)

count = 0
nums = 0
for line in fhandel:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    else:
        # line = line.rstrip()
        count = count + 1
        values = line[line.find('0'):] # <-string slicing, starting from found '0' to the last index value
        # print(values)
        values = float(values)
        nums = nums + values
# print(count)
print("Total average:", nums / count)
print("Done.")
