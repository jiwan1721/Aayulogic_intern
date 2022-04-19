file = open('jiwan.txt','w')
file.write(" hero baneko hora")
#print(file.read())

# for item in file:
#     print(item)
# #file = open('jiwan.txt','W')

# #file.write(" hero baneko")
# #print(file.read())
# #file.write("write something")
# # for item in file:
# #     print(item)
# with open('jiwan.txt','w') as file:
#     file.write("write function use gareko")
# import csv
# file_csv = open('bsic.csv','r')
# dict_from_csv = {}
# reader = csv.reader(file_csv,1)
# dict_from_csv= {rows[0]:rows[1] for rows in reader}
# dict_from_csv.pop("book_name")
# print(dict_from_csv)
# # for item in file_csv:
# #     if book
# less_than_hundrade = {}
# greater_than_hundrade = {}
# greater_than_twoHundrade = {}
# x = list(dict_from_csv.values())
# print(x)

# for item in dict_from_csv:
    
#     for i in x:
            
#         if i <100:
#             less_than_hundrade.update(item)
#         elif 100<i<=200:
#             greater_than_hundrade.update(item)
#         elif i>200:
#             greater_than_twoHundrade.update(item)
        
# print(less_than_hundrade)
# print(greater_than_hundrade)
# print(greater_than_twoHundrade)



def file_func(file):

    file = list(file_csv)
    for index, item in enumerate(file):
        if index == 0:
            less_2 = open('les_200.csv','w+')

            less_hundred = open('less_than_hundrade.csv','w+')

            greater_200 = open('greater_200.csv','w+')
            less_2.write(item)
            continue
        
        
        
        price=int(item.split(",")[1])
    
    
    
        if price<=100:
            
            less_hundred.write(item)
        elif price<=200:
            
            less_2.write(item)
        else:
            greater_200.write(item)
            
        
file_csv = open('bsic.csv','r+')

file_func(file_csv)