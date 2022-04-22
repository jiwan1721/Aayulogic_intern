import random
def get_random_number():
        return random.randint(0,100)

def start_game():
        random_number = get_random_number()

        print(
            f"Guess the randomly generated number from {0} to {100}")
        chances = 0

    
        MAX_CHANCES = 10
        
        while True:
            if chances == MAX_CHANCES:
                user_number = int(input("Enter the guessed number: "))
                if user_number == random_number:
                    print(
                        f"-> Hurray! You got it in {chances + 1} step{'s' if chances > 1 else ''}!")
                    break
                elif user_number < random_number:
                    print("-> Your number is less than the random number")
                else:
                    print("-> Your number is greater than the random number")
                chances += 1

start_game()