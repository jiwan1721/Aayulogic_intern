statement = "i love football jiawan hawa"
statement1 = "i don,t love football football pani"

def similar_func(state1,state2):
    state1=state1.split()
    state2=state2.split()
    list1=[]
    list2=[]
    for item in state1:
        if item in state2:
            list1.append(item)
        else:
            list2.append(item)
    print("similar item",list1)
    for item in state2:
        if item not in state1:
            list2.append(item)
        
    
    print("different item", list2)

similar_func(statement, statement1)

def different_compare(common,extra):
    common = common.split()
    extra= extra.split()
    my_list = common+extra
    common_list = []
    extra_list = []
    
    for item in my_list:
        my_list_with_count = my_list.count(item)
        if my_list_with_count>1:
            common_list.append(item)
        if my_list_with_count==1:
            extra_list.append(item)
    print("common: ",set(common_list))
    print("extra: ",extra_list)
different_compare(statement, statement1)
