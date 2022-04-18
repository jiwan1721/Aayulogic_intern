def userlist(duplicate_value):
    my_list2 = []
    my_list3 = []
    for item in duplicate_value:
        if item not in my_list2:
            my_list2.append(item)
        else:
            my_list3.append(item)
            
    print(my_list3)

def ReverseFunc(user_list_1):
    reverse_list = []
    for item in user_list_1:
        reverse_list.insert(0, item)
    print(reverse_list)
        


user_list = [1,2,2,3,3,4,5,5]
userlist(user_list)
ReverseFunc(user_list)



