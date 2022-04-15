
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
    print(TO_DO_lIST)
    del TO_DO_lIST
    print("list is deleted")

print("type '0' to create list  \ntype '1' update by index  \ntype '2' to delete by index list \ntype '3' to delete list: ")

try:
    user_input =int((input("enter number: ")))
    if 0<=user_input<=2:
        if user_input==0:
            list_input=input("enter list: ")
            create_list(list_input)
            try:
                user_input =int((input("enter number: ")))
                if user_input==1:
                    index_input = int(input("enter index number: "))
                    number_input = input("enter the number you want to update: ")
                    update_list(index_input,number_input)
                elif user_input==2:
                    delete()
            except ValueError:
                print("give integer input")
        else:
            print("first enter '0' please: ")
    else:
        print("type correct number please: ")
except ValueError:
    print("only give input of integer")