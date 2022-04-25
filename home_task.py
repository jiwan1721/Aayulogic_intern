# import csv
# file = open('homework.csv','r+')
# reader = csv.reader(file)

# for line in csv.DictReader(reader):
#    print(line)
# #file = 'homework.csv'
# def print_dictionary(file):
    
#     with open(file) as data:
#         for line in csv.DictReader(data):
#             print(line)
    

# for rows in reader:
#         k = rows[0]
#         v = rows[1]
#         mydict = {k:v for k, v in rows}
#     print(mydict)
            



# print_dictionary(file)
# import csv

# new_data_dict = {}
# with open("homework.csv", 'r') as data_file:
#     data = csv.DictReader(data_file, delimiter=",")
#     for row in data:
#         item = new_data_dict.get(row["name"], dict())
#         item[row["address"]] = int(row["gender"])

#         new_data_dict[row["name"]] = item

# print(new_data_dict)
# fhandle = open('homework.csv')
# reviews={}
# for line in fhandle:
#     words = line.split(',')
#     reviews.update({words[0]: {}})
#     n = len(words)
#     for i in range(1, n-1, 2):
#         if words[0] in reviews.keys():
#             reviews[words[0]].update({words[i]:words[i+1]})
# print(reviews)

file = open('homework.csv','r')
file = list(file)


def user_detail():
    
    user_dtl = []
    for item in file[1:]:
        user_list_splited = item.split(",")
        name = user_list_splited[0]
        address = user_list_splited[1]
        gender = user_list_splited[2]
        district = ""

        if len(address.split(" ")) == 2:
            district = address.split(" ")[1]
                
        
            user_info = {
                    'name':{
                        'first_name':name.split(" ")[0],
                        'lastname':name.split(" ")[1]
                    },
                    'address':{
                        'location':address.split(" ")[0],
                        'district': district
                    },
                    'gender': gender[:-1]
            }
                
        user_dtl.append(user_info)
    return user_dtl

print(user_detail())
        

def user_detail_kathmandu(district_ktm):
    district = user_detail()
    ktm_list = []
    print(district)
    for item in district:
        
        if item['address']['district']== district_ktm:
            
            ktm_list.append(item)
            
        else:
            print("not found")
    return ktm_list
    



print(user_detail_kathmandu('kathmandu'))




# reader1 = csv.reader(file)

# people = {}
# details=[]
# for row in reader1:
#     people[row[0]]={
#         'address':row[1],
#         'gender':row[2]
#         }
    
# print(people)
#first load the file
