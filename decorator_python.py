def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def greet(func):
    greeting = func("hello Baby how are you")
    print(greeting)
greet(shout)
greet(whisper)

def create_adder(x):
    def adder(y):
        return x+y
    return adder
add_num= create_adder(18)
print(add_num(10))

def hello_dec(func):
    def inner1():
        print('before execution')
        func()
        print("this is after function")
    return inner1
def func_to_used():
    print("this is inside func")

func_to_used = hello_dec(func_to_used)


func_to_used()