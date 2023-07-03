# reading romeo.txt counting the five most used words and printing by using tuples

fname = input("Enter file name: ")
fhandle = open(fname)

count = dict()  # creating an empty dictionary to assign keys and values
for line in fhandle:
    words = line.split()  # splitting each word within a list creating keys
    for number in words:
        count[number] = count.get(number, 0) + 1  # counting the keys to assign values to the keys
    # print(count)

# creates an empty list and sorts by using "sorted([])"
# tuple (v,k) is the assigned keys and values from count.items
s_list = sorted([(v, k) for k, v in count.items()])
s_list.reverse()  # reverses list order to have largest values to smallest values

# prints only the 5 most used words and how many times used
for v, k in s_list[:5]:
    print("Word:", k, "\nValue:", v)
