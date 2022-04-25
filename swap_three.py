a = 30
b = 400
def asdfadf():
    print("afasdfa sdf sadfsadf sadf")
asdfadf()
if __name__ == "__main__":
    print("adfsadfasdf asdfsadf adsfasdf")


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%400 ==0 or year%4 ==0 :
        return True

    
    return leap

year = int(input())
print(is_leap(year))
