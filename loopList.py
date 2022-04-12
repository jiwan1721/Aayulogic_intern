list1 = ["banana","mango", "orange","apple","cherry"]
# print item in the list , one by one
for x in list1:
    print(x)


# print all item by referring their index
for i in range(len(list1)):
    print(list1[i])



# using while loop
i = 0
while i< len(list1):
    print("using while loop")
    print(list1[i])
    i = i + 1

for j in range(10):
    print("j")
    print(j)

[print(x) for x in list1]
new_list = []
for x in list1:
    if "n" in x:
        new_list.append(x)
print(new_list)
new_list2 = [x for x in list1 if "o" in x]
print(new_list2)
new_list3 = [x for x in list1]
print("new list is ",new_list3)
print(list1)
newlist4 = [x for x in list1 if x != "apple"]
print(newlist4)

new_range = [x for x in range(10)]
print(new_range)

list2 = ['a','b','c','d','c','d']
newlist2 = [x if x !='c' else 'e' for x in list2]
print(newlist2)
newlist12 = [x.upper() for x in list1]
print(newlist12)


'''
list_11 = ['a','v','h','k','d']
list_11n = []
for x in list_11:
    x.sort()
    list_11n.append(x)
print("list n ", list_11)

print(list_11)
list_11.sort()
print(list_11)'''


def myfunc(n):
    return abs(n - 34)

thislist = [34,35,46,56,43,45,76,58]
thislist.sort(key=myfunc)
print(thislist)
thislist.sort(reverse=True)
print(thislist)