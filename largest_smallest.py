# user types any number as much as possible until they stop by typing done

largest = None
smallest = None

print("Enter any number. Type (Done) to quit.")
print("The largest and smallest number typed will be printed.")

while True:
    num = input("Enter any number: ").capitalize()

    if num == "Done":
        break

    try:
        i_num = int(num)
    except:
        continue

    if largest is None:
        largest = i_num
    if largest < i_num:
        largest = i_num

    if smallest is None:
        smallest = i_num
    if smallest > i_num:
        smallest = i_num

print("\nLargest:", largest)
print("\nSmallest:", smallest)
