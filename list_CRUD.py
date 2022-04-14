input_1 = input("enter list: ")
list_1 =  input_1.split()
print("your list is: ", list_1)
input_2 = input("update list: ")
list2 = input_2.split()
list_1.extend(list2)
print("your updated list: ",list_1)
print("length of list ",len(list_1))
try:
  input_3 = int(input("delete list by index number: "))
  print("deleted list element  is: ",list_1[input_3])

  list_1.pop(input_3)
  print("after deleting index no:",input_3,"list element",list_1)
except:
    print("type correct index"," less than: ",len(list_1))


input_4 = input("type 'delete' to delete list: ")
if input_4=="delete":
    del list_1
    print("list is deleted: ")
else:
    print("type correct keyword")