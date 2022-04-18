def aginDuplicate(input_user):

    list1=[]
    for item, duplicate in enumerate(input_user):
        if item not in list1:
            duplicate.append(item)
        else:
            list1.append(item)
    print(list1)

user_list = input("enter list")
user_list.split()
aginDuplicate(user_list)