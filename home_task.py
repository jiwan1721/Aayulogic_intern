from asyncore import read
import csv
file = open('homework.csv','r')
reader = csv.reader(file)
for i in reader:
    print(i)
# dict_from_csv = {rows[0]:rows[2] for rows in reader}
# print(dict_from_csv)
for line in csv.DictReader(reader):
    print(line)
# #file = 'homework.csv'
# def print_dictionary(file):
#     file = (file)
#     print(file)
#     # with open(file) as data:
#     #     for line in csv.DictReader(data):
#     #         print(line)
    
#     for index, item in enumerate(file):
#         print(index)
#         new_dict = item.split(',')
#         print(new_dict)
#         for index1, item1 in enumerate(new_dict):
#             print(item1)    

# for rows in reader:
#         k = rows[0]
#         v = rows[1]
#         mydict = {k:v for k, v in rows}
#     print(mydict)
            



# print_dictionary(file)