

def function(input_num):
    return 150-input_num


#using dictuionary 
def function1(input_num):
    return {50:100,100:50}.get(input_num)

#using return function in 
def function2(input_num):
    return 50 if input_num==100 else 100 if input_num==50 else None

print(function2(50))