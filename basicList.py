first_list = ["one","two","three"]
print(first_list)
for i in range(len(first_list)):
    print("index",i,"value",first_list[i])

list_one = ["banana", "banana","banana","banana"]# it allows duplicate values
print(list_one)
print(len(list_one))

#list with different data types
list1 = ["hero","villan",list_one]
list2 = [1,2,3,4,56,6]
list3 = [True,False,True]
print(list1)
print(list2)
print(list3)

list4 = ["jiwan",9866290300,"male",28]
print(list4)
print(type(list4))

#indexing of 
#python indexing starts with 0
list_index = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list_index[2])#printing third value of list

print(list_index[2:5]) #it starts with 2 included and ends with 5 not included
#index 2 dekhi 5 samma ko valuue print garnu paryo vane

print(list_index[:4]) # 4 index vanda agadiko value haru print garnu paryo vane

print(list_index[4:]) # 4 index vanda paxi ko valu print garnu paryo vane

print(list_index[-6:-1]) # index 4 dekhi 6 samma ko value print garxa

list_index[1]= "banana1"
print(list_index[1])

list_index[0:3]= ["orange1","kiwi2"]
print(list_index)
print(list_index[0],list_index[3])
print(list_index)
list_index.insert(2, "new value") # 2 index ma add garxa
print(list_index)
print(list1)
list1.append("mangos") # append le last ma add garxxa
print(list1)

#extend two lists
print(list3)
list3.extend(list4)
print(list3)
list3.remove(28)
print(list3)
list3.pop(0)# index 0 ko item remove garxa
print(list3)
list3.pop()# last ko item remove garxa
print(list3)

del list3[0] # specified index laii delete garxa
print(list3)

list3.clear()
print(list3)
