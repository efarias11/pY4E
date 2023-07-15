# using regular expression to read py4e-data.dr-chuck.net_regex_sum_42.txt
# and calculate a sum from the text
import re
fh = open('py4e-data.dr-chuck.net_regex_sum_42.txt')

lst = list()
for line in fh:
    #line = line.rstrip()
    nums = re.findall('[0-9]+', line)  # looks for all string numbers
    if not nums:  # continues pass strings that aren't numbers
        continue
    lst.extend(nums)  # Use extend() instead of append() to add individual numbers, not sublists

# print(lst)
lst = [int(num) for num in lst]  # Convert the numbers in lst to integers
# (need to structure like this so the ints can be iterable)

print(sum(lst))  # note this just prints the sum (doesn't change numbers in the background)
