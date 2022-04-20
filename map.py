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

name_List = ['jiwan','hero','jack','john','hand']
def names_j(name_List):
    name = []
    different =[]
    name_first=[]
    for item in name_List:
        name_first.append(item[0])
    print(name_first)
    for item in name_List:
        if item[0]==name_first:
            name.append(item)



        
    print(name)
    print(different)
    

names_j(name_List)