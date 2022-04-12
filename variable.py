x = 4
x = "hello"
print(x)

x = "i  m awsome"
def funct():
    print(" i am jiwan and"+x)
funct()


y = "hello how are you"
def funct1():
    y = "fantstic"
    print("i am jiwan and"+x)
funct1()
print("python" + y)

def globFunction():
    global z
    z = "fantastic"
globFunction()

print("python is "+z)

a = "hello"
def func2():
    global a
    a = " hi"
func2()
print(" hello", a)


def func3():
    global x
    x = "hi"
    print("hello 123 ", x)
func3()
print(x)