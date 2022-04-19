
TO_DO_lIST = []

def tryException():
    try:
        print()
    
    except ValueError:
        print("give integer only: ")

def create_list():
    list_input=input("enter list: ")
    list_input=list_input.split()
    TO_DO_lIST.extend(list_input)
    print("your list is: ",TO_DO_lIST)
    return TO_DO_lIST

def update_list():
    try:
        index_number = int(input("enter index number: "))
    except ValueError:
        print("give input integer only: ")
        number = input("enter the number you want to update: ")
        #create_list(pop(index_number))
        # upadate_index = create_list(insert())
        TO_DO_lIST.pop(index_number)
        TO_DO_lIST.insert(index_number,number)
        print("updated list",TO_DO_lIST)
    
       
    
def delete():
    delete_list =[]
    delete_list.extend(TO_DO_lIST)
    del delete_list
    print("list is deleted")

def delete_index():
    try:
        del_index_no = int(input("give index no you want to delete: "))
        print("deleted number is: ", TO_DO_lIST[del_index_no])
        TO_DO_lIST.pop(del_index_no)
        print("after deleting num", TO_DO_lIST)
    except ValueError:
        print("give integer only: ")
            

print("type '0' to create list  \ntype '1' update by index  \ntype '2' to delete by index list \ntype '3' to delete list: ")

try:
    user_input =int((input("enter number: ")))
except ValueError:
    print("only give input of integer")
    if 0<=user_input<=2:
        if user_input==0:  
            create_list()
            try:
                user_input_operation =int((input("enter number: ")))
            except ValueError:
                print("give integer input")
            if user_input_operation==1:      
                update_list()
            elif user_input_operation==2:
                delete()
            elif user_input_operation==3:
                delete_index()        
        else:
            print("first enter '0' please: ")
    else:
        print("type correct number please: ")
