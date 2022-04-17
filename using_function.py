
TO_DO_lIST = []
def create_list(list1):
    list1 =list1.split()
    
    
    TO_DO_lIST.extend(list1)
    print("your list is: ",TO_DO_lIST)
    
    return TO_DO_lIST

def update_list(index_number, number):
    #create_list(pop(index_number))
   # upadate_index = create_list(insert())
    TO_DO_lIST.pop(index_number)
    TO_DO_lIST.insert(index_number,number)
    print("updated list",TO_DO_lIST)
    
def delete():
    delete_list =0
    delete_list.extend(TO_DO_lIST)
    del delete_list
    print("list is deleted")

def delete_index(del_index_no):
    print("deleted number is: ", TO_DO_lIST[del_index_no])
    TO_DO_lIST.pop(del_index_no)
    print("after deleting num", TO_DO_lIST)

print("type '0' to create list  \ntype '1' update by index  \ntype '2' to delete by index list \ntype '3' to delete list: ")

try:
    user_input =int((input("enter number: ")))
    if 0<=user_input<=2:
        if user_input==0:
            list_input=input("enter list: ")
            create_list(list_input)
            try:
                user_input_operation =int((input("enter number: ")))
                if user_input_operation==1:
                    try:
                        index_input = int(input("enter index number: "))
                        number_input = input("enter the number you want to update: ")
                        update_list(index_input,number_input)
                    except ValueError:
                         print("only give input of integer")
                elif user_input_operation==2:
                    delete()
                elif user_input_operation==3:
                    delete_index()
            except ValueError:
                print("give integer input")
        else:
            print("first enter '0' please: ")
    else:
        print("type correct number please: ")
except ValueError:
    print("only give input of integer")