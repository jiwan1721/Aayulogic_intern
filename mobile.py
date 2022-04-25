file = open('mobile.csv','r')
file = list(file)
def mobile_category():
    mobile_detail = []
    samsung_list=[]
    apple_list = []
    Mi_list = []
    mobile_dict ={}
  
    
    for row in file[1:]:
        row_splited = row.split(",")
        
        category_splited = row_splited[0]
        name_splited = row_splited[1]
        description_splited = row_splited[2]
        tag_splited = row_splited[3]
        price_splited = row_splited[4]
        
        # if category_splited=='samsung':
        #     samsung_dict={
        #             'name':name_splited,
        #             'description':description_splited,
        #             'tag':tag_splited,
        #             'price':price_splited[:-1]  
        #     }
        #     samsung_list.append(samsung_dict)
        # if category_splited=="apple":
        #     apple_dict={
                
        #         'name':name_splited,
        #         'description':description_splited,
        #         'tag':tag_splited,
        #         'price':price_splited[:-1]
        #     }
        #     apple_list.append(apple_dict)
        # if category_splited=="MI":
        #     MI_dict={
        #             'name':name_splited,
        #             'description':description_splited,
        #             'tag':tag_splited,
        #             'price':price_splited[:-1]
        #     }     
        #     Mi_list.append(MI_dict)
        # mobile_dict = {
            
        #         'apple':apple_list,
        #         'samsung':samsung_list,
        #         'Mi':Mi_list
            
        # }
        mobile_detail.append(category_splited)
    return set(mobile_detail)
def search_by_nmae(name):
    name_list = []
    for item in file[1:]:
        namelist = item.split(",")
        searched_name = namelist[1]
        print(searched_name)
        if searched_name ==name :
            name_dict ={
                namelist[0]:{
                    'name':searched_name,
                    'description':namelist[2],
                    'tag':namelist[3],
                    'price':namelist[4][:-1]
                }
            }
            name_list.append(name_dict)
        else:
            print("not found")
    return name_list
    
def menu():
    user_input = int(input('enter 1 to see category: \nenter 2 to search by name \nenter 3 to search \nenter 4 to filter by price\nenter here: '))
    if user_input ==1:
        print(mobile_category())
    elif user_input ==2:
        user_input2 = input("please give name of device: ")
        search_by_nmae(user_input2)
    elif user_input ==3:
        user_input3 = input("type anaything you want to search: ")
    elif user_input ==4:
        pass

menu()


            


