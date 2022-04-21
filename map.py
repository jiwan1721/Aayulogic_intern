# def addition(a,b):
#     return a+b
# numbers = (1,2,3,4,5,6,7,8,0,3)
# number= (1,3,5,6,7,8,9,0)
# result = map(addition, number,numbers)
# print(list(result))
# num3 = number+numbers
# print(num3)

# def lamb_func(number,numbers):
#     result_1 = map(lambda x,y:x+y,number,numbers)
#     print("run",list(result_1))
# lamb_func(number,numbers)


#polymorphism concept ho yo
def add(a,b,c=0):
    return a+b+c

print(add(3,3,5))
print(add(2, 3))
# try:
name_List = ['jiwan','hero','jack','john','hand','rakesh','']
#     if not name_List:
#         raise ValueError('empty string')
# except ValueError as e:
#     print(e)
def names_j(name_List):
 
    name_first={}
    try:

        for item in name_List:
            if item[0] not in name_first:              #Details["Age"] += [20, "Twenty"]
                name_first[item[0]]=[item]
            else:
                    name_first[item[0]].append(item)
        
        
        
        print(name_first)
    except IndexError:
        print("index rakhna bey")


    # for item in name_first:
    #     if item[0]:
    #         different.append(item)
    # res = dict(zip(set(different),name_List))

    # print(different)
    # print(str(res))

    #key = set(different)
    #print(key)
    

names_j(name_List)