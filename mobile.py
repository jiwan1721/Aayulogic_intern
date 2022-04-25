file = open('mobile.csv','r')
file = list(file)
def mobile_category():
    mobile_detail = []
    samsung_list=[]
    apple_list = []
    Mi_list = []
  
    
    for row in file[1:]:
        row_splited = row.split(",")
        
        category_splited = row_splited[0]
        name_splited = row_splited[1]
        description_splited = row_splited[2]
        tag_splited = row_splited[3]
        price_splited = row_splited[4]
        if category_splited=='samsung':
            samsung_dict={
                    'name':name_splited,
                    'description':description_splited,
                    'tag':tag_splited,
                    'price':price_splited[:-1]  
            }
            samsung_list.append(samsung_dict)
        if category_splited=="apple":
            apple_dict={
                'name':name_splited,
                'description':description_splited,
                'tag':tag_splited,
                'price':price_splited[:-1]
            }
            apple_list.append(apple_dict)
        if category_splited=="MI":
            MI_dict={
                    'name':name_splited,
                    'description':description_splited,
                    'tag':tag_splited,
                    'price':price_splited[:-1]
            }     
            Mi_list.append(MI_dict)
        mobile_dict = {
            'category':{
                'apple':apple_list,
                'samsung':samsung_list,
                'Mi':Mi_list
            }
        }
    mobile_detail.append(mobile_dict)
    return mobile_detail

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
    

print(search_by_nmae('Iphone10'))
            


