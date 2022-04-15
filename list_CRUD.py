try:

    main_user=int(input("type '0' to create list  \ntype '1' update by index  \ntype '2' to delete by index list \ntype '3' to delete list: "))
    if main_user>=0 and main_user <=3:
    

        input_1 = input("enter list: ")
        list_1 =  input_1.split()
        print("your list is: ", list_1)
        main_user1 = int(input("choose what yout want to do: "))
        try:
            if main_user1==1 or main_user==1:
               input_2 = int(input("enter index number: "))
               input_3 = input("enter number to change: ")
               list_1.pop(input_2)
               list_1.insert(input_2,input_3)
               print(list_1) 
               print("updated number",input_3)
            elif main_user1==2 or main_user==2:
               input_4 = int(input("give index number: "))
               print("value deleted",list_1[input_4])
               list_1.pop(input_4)
               print(list_1)
            elif main_user1==3 or main_user==3:
               del list_1
               print("list is deleted")
        except ValueError:
            print("please give integer input")
    
    else:
        print("type correct number, please")
except Exception as e:
        print(e)  




'''
input_2 = input("update list: ")
list2 = input_2.split()
list_1.extend(list2)
print("your updated list: ",list_1)

'''

'''print("type '0' to create list  \ntype '1' update by index  \ntype '2' to delete by index list \ntype '3' to delete list: ")
user_input = int(input("enter number: "))
if 0<=user_input<=3:
    if user_input==0:
        create_input = input("enter list: ")
        list1 = create_input.split()
        print(list1)
    elif user_input==1:
        delete_index = int(input("enter index: "))
        list1.pop(delete_index)
        print(list1)'''