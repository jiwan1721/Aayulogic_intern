import csv
file = open('homework.csv','r+')

#file = 'homework.csv'
def print_dictionary(file):
    file = (file)
    print(file)
    # with open(file) as data:
    #     for line in csv.DictReader(data):
    #         print(line)
    for index, item in enumerate(file):
        print(index)
        new_dict = item.split(',')
        print(new_dict)
        for index1, item1 in enumerate(new_dict):
            print(item1)



print_dictionary(file)