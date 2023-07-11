# reading vowels from a string sentence by using regular expressions
# counting and totaling the read vowels
import re

count = dict()
s = "My 2 favorite numbers are 19 and 42"
vf = re.findall('[aeiou]', s)
# print(vf)
for letter in vf:
    count[letter] = count.get(letter, 0) + 1

lst = list()
for (k, v) in count.items():
    lst.append((k, v))

lst.sort()
for k, v in lst:
    print("Vowel:", k, "Count", v)
