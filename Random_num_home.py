import random



def number_guess():
    random_number = random.randint(0, 100)
    print(random)
 
    no_of_guess = 5
    print("guesss number between {0} and {100}")
    for chances in range(no_of_guess):
        try:
            first_input = int(input("enter your number: "))
        except ValueError:           
            print("please type integer only")
    
        if first_input==random_number:
            no_of_guess-=1
            print(f"congratulation yo have gussed in  {no_of_guess} time")
            
            return first_input
        elif first_input<random_number<=100:
            no_of_guess-=1
            print(f"you have {no_of_guess} left")
            print("your input is lesss than randon number: ")
        elif first_input>random_number<=100:
            no_of_guess-=1
            print(f"you have {no_of_guess} left")
            print("input is greater than random number: ")
    
        if no_of_guess==0:
            print("you lose, better luck next times")
            print(f"the number is {random_number}")

            input_user = input("do you want to play again: ")
            if input_user=="yes":
                number_guess()
            else:
                return


number_guess()