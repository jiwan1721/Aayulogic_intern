D1 = {
    "name": "jiwan",
    "age": 1000,
    "phone": 12343546,
    "age":133, # it will override the above age value
    "color":['red','green','white']
}
print(D1)
type(D1)
print(D1["name"],D1["age"])
print(len(D1))

#get the value of key name
x = D1["color"]
print(x)
# there is another way to do that
y = D1.get("name")# this method is long
print(y)

# GET KEYS
z = D1.keys()
print(z)
D1["last_name"]= "chand"
print(D1.keys())
print(D1)
a = D1.values()
print(a)

D1["name"]="jiwan kumar"
print(D1)

b = D1.items()
print(b)

if "name" in D1:
    print("yes, exists in dictionary")
else:
    print("no")

if "name1" in D1:
    print("yes, exists in dictionary")
else:
    print("no")

print(D1)
D1.pop("color")
print(D1)
D1.popitem() # it remove the item from the last
print(D1)
del D1['age'] # removes specific key
print(D1)

D1.clear() # dictionary laii clear garxa
print(D1)
del D1
