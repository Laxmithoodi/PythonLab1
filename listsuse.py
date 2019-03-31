def max_num_in_list( list ):
    max = list[ 0 ]
    for x in list:
        if x > max:
            max = x
    return max
print(max_num_in_list([10, 78, 0, -8, 15]))


alist = [0, 10, 20, 40, 5, 9]
blist = list()
for item in alist[::-1]:
    blist.append(item)
print("New reversed list numeric: ", blist)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruitslist = list()
for item in fruits[::-1]:
    fruitslist.append(item)
print("New reversed list:", fruitslist)


fruitslist = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

if 'pear' in fruitslist:
    print("Yes, found the string:", fruitslist)
else:
    print("Element not found")


checklist = [2, 3, 4, 5, 6, 7]
oddlist = []
count = 0
for i in checklist:
    if count % 2 == 1:
        oddlist.append(i)
    count += 1
print("new list with odd index elements: ", oddlist)

a = range(10)
runningTotal = []
tot = 0
for item in a:
    tot += item
    runningTotal.append(tot)
print(runningTotal)




