detail = {
    'name':'jiwan',
    'lastname':'chand',
    'email':'chandjiwn9@gmail.com',
    'phone':455465456
}
for x in detail:
    print(x)
for x in detail.items():
    print(x)

for x in detail.values():
    print(x)

for x in detail.keys():
    print(x)

for x, y in detail.items():
    print(x,y)

copy_detail = detail.copy()
print(copy_detail)
copy_detail_again = dict(copy_detail)
print(copy_detail_again)

# NESTED DICTIONARY
info = {
    'client1':{
        'name':'jiwan',
        'age':19
    },
    'client2':{
        'name':'depesh',
        'age':'sweet sixteen'

    }
}
print(info)
for x,y in info.items():
    for a,b in info.items():
        print(a,b)
    print(x,y)

new_dict = {
    'detail':detail,
    'info':info
}
print(new_dict)

list1 = [1,2,3,4]
list2 = [2,3,4,5]
list3=[]
for i in range(0,len(list2)):
    list3.append(list2[i]+list1[i])
print("adding list number : ",list3)
for i in range(0, len(list1)):
    list3.append(list1[i]+list2[i])
   
print("adding two lists: ",list3)
for i in list2:
    list1.append(i)
print("joining two lists: ", list1)

print(list1)
newlist2 = []
list1 = [1,2,3,4,5,6,7,8,9,10]
for x in list1:
    if x%2 == 0:
       newlist2.append(x)
print("even numbers: ",newlist2)

list1 = [1,2,3,4]
list2 = [2,3,4,5]
list1.extend(list2)
print(list1)
list1 = [1,2,3,4]
list2 = [2,3,4,5]
list3= list1+list2
print(list3)