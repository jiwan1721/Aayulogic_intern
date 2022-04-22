# import random
class game:
    raise_ammomt= 1.4
    def __init__(self,name,age,pay):
        self.name=name
        self.age = age
        self.pay = pay
    def name_age(self):
        return '{}{}'.format(self.name,self.age)
    def apply_raise(self):
        self.pay = int(self.pay*game.raise_ammomt)
    @classmethod
    def set_raise_ammount(cls,ammount):
        cls.raise_ammomt=ammount
obj = game('jiwan ', 45,10000)
# print(obj.name_age())
# print(obj.pay)
# obj.apply_raise()
# print(obj.pay)
# print(obj.__dict__)
game.set_raise_ammount(1.5)
print(game.raise_ammomt)
print(obj.raise_ammomt)
#sentence = input("sentence dena bey: ")
#vowels = [x for x in sentence if x in "aeiouAEIOU"]
#print(set(vowels))
import datetime
today = datetime.datetime.today()
print(f"time= {today:%D %d %Y}")
print(today)

#     def number_guess(self):
#         random_number = random.randint(0, 100)
#         print(random_number)
 
#         no_of_guess = 5
#         print("guesss number between {0} and {100}")
#         for chances in range(no_of_guess):
#             try:
#                 first_input = int(input("enter your number: "))
#             except ValueError:           
#                 print("please type integer only")
        
#             if first_input==random_number:
                
#                 print(f"congratulation yo have gussed in  {chances} time")
#             elif first_input<random_number<=100:
#                 no_of_guess-=1
#                 print(f"you have {no_of_guess} left")
#                 print("your input is lesss than randon number: ")
#             elif first_input>random_number<=100:
#                 no_of_guess-=1
#                 print(f"you have {no_of_guess} left")
#                 print("input is greater than random number: ")
        
#             if no_of_guess==0:
#                 print("you lose, better luck next times")
#                 print(f"the number is {random_number}")

#                 input_user = input("do you want to play again: ")
#                 if input_user=="yes":
#                     self.number_guess()
#                 else:
#                     return
# obj = game()
# obj.number_guess()

