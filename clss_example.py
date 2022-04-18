class Basic:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("hello my name is: ",self.name)

B1 = Basic("jiwan", 199)
B1.myfunc()
print(B1.name)
print(B1.age)
B1.age = 1000
print(B1.age)
del B1.age # it is used to delete the property
del B1   # it is used to delete whole object


class child_Class(Basic):
    def __init__(self, name, age,year):
        Basic.__init__(self, name, age)
        #super().__init__(name, age)        # choose one its same
        self.dob = year
    def welcome(self):
        print("Dear ",self.name,"your age is: ",self.age,"your birthdate: ",self.dob)


x = child_Class("RAM",19,1222)
x.myfunc()
x.welcome()
print(x.dob)