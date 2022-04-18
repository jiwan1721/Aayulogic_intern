list1 = [1,2,4,5,6,7,8,8]

for i in list1:
    if i%2==0:
        print(i)
    i = i+1

list2 = [1,2,4,5,6,7,8,8]
for i, x in enumerate(list2):
    if i%2 ==0:
        print(x)

'''for i in enumerate(list2):
    if i%2 ==0:
        print(i)'''
