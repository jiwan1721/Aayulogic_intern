detail = {
    'name':'jiwan',
    'lastname':'chand',
    'email':'chandjiwn9@gmail.com',
    'phone':455465456
}
for x in detail:
    print(x)
for x in detail.items():
    print(x)

for x in detail.values():
    print(x)

for x in detail.keys():
    print(x)

for x, y in detail.items():
    print(x,y)

copy_detail = detail.copy()
print(copy_detail)
copy_detail_again = dict(copy_detail)
print(copy_detail_again)

# NESTED DICTIONARY
info = {
    'client1':{
        'name':'jiwan',
        'age':19
    },
    'client2':{
        'name':'depesh',
        'age':'sweet sixteen'

    }
}
print(info)
for x,y in info.items():
    for a,b in info.items():
        print(a,b)
    print(x,y)

new_dict = {
    'detail':detail,
    'info':info
}
print(new_dict)