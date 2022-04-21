import csv

file_path = 'homework.csv'
people_list = []
headers_list = []

index = 0

with open(file_path, 'r') as data:
    for line in csv.reader(data):
        index += 1
        if index < 1:
            people_dict = {}
            for i, elem in enumerate(headers_list):
                people_dict[elem] = line[i]
                people_list.append(people_dict)
        else:
            headers_list = list(line)
print(people_dict)