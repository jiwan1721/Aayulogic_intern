import random


def number_guess():
    random_number = random.randint(0, 100)
    print(random_number)
    first_input = int(input("enter your number: "))
    if first_input==random_number:
        print("your are right \nyour random number is: ",random_number)
        return first_input
    elif first_input<random_number:
        print("your input is lesss than randon number: ")
    elif first_input>random_number:
        print("input is grater than random number: ")
    else:
        print("plese enter number between 0 to 100")
    print("you have left 4 choices")
    second_input = int(input("enter your number: "))
    if second_input==random_number:
        print("your are right \nyour random number is: ",second_input)
        return second_input
    elif second_input<random_number:
        print("your input is lesss than number: ")
    elif second_input>random_number:
        print("input is grater than number: ")
    else:
        print("plese enter number between 0 to 100")
    print("you have 3 choice left")
    third_input = int(input("enter your number: "))
    if third_input==random_number:
        print("your are right \nyour random number is: ",third_input)
        return third_input
    elif third_input<random_number:
        print("your input is lesss than random number: ")
    elif third_input>random_number:
        print("input is grater than random number: ")
    else:
        print("plese enter number between 0 to 100")
    print("you have 2 choice left")
    fourth_input = int(input("enter your number: "))
    if fourth_input==random_number:
        print("your are right \nyour random number is: ",fourth_input)
        return third_input
    elif fourth_input<random_number:
        print("your input is lesss than random number: ")
    elif fourth_input>random_number:
        print("input is grater than random number: ")
    else:
        print("plese enter number between 0 to 100")
    print("you have 2 choice left")
    fifth_input = int(input("enter your number: "))
    if fifth_input==random_number:
        print("your are right \nyour random number is: ",fifth_input)
        return third_input
    elif fifth_input<random_number:
        print("your input is lesss than random number: ")
    elif fifth_input>random_number:
        print("input is grater than random number: ")
    else:
        print("plese enter number between 0 to 100")
    print("you have 1 choice left")
    sixth_input = int(input("enter your number: "))
    if sixth_input==random_number:
        print("your are right \nyour random number is: ",sixth_input)
        return sixth_input
    elif sixth_input<random_number:
        print("your input is lesss than random number: ")
    elif sixth_input>random_number:
        print("input is grater than random number: ")
    else:
        print("plese enter number between 0 to 100")
    return 'number is: ', random_number


