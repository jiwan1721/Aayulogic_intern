def vowel(texts):
    vowel_input = ['a','e','i','o','u','A','E','I','O','U']
    for i in texts:
        if (i in vowel_input): 
            return True
        else:
            return False
sequence = ['ae','b','c','d','e','f','g','h']
text_12 = "hello my name is jiwan chanda"
text_next = []



filtered = filter(vowel,text_12)
text_next.extend(filtered)
print(set(text_next))

# # function that filters vowels
# def fun(variable):
#     letters = ['a', 'e', 'i', 'o', 'u']
#     if (variable in letters):
#         return True
#     else:
#         return False
 
  
# sequence
# sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
  
# # using filter function
# filtered = filter(fun, sequence)
  
# print('The filtered letters are:')
# for s in filtered:
#     print(s)
# ages = [5, 12, 17, 18, 24, 32]
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True
less = []
adults = filter(myFunc, ages)
less.extend(adults)
print(less)




