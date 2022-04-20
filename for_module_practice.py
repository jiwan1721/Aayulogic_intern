def find_num(n):
    a,b = 0,1
    while a<n:
        print(a,end=' ')
        a,b = b,a+b
    print()

def find_numbers_2(n):
    result = []
    a,b = 0,1
    while a<n:
        result.append(a)
        a,b = a,a+b
    return result