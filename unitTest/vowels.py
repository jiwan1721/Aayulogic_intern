def get_vowels(vowels):
    vowel_letter = ['a','e','i','o','u']
    vowel_letters = []
    constant_letter = []
    for letter in vowels:
        if letter in vowel_letter:
            vowel_letters.append(letter)
        else:
            constant_letter.append(letter)
    return vowel_letters


# string = str(input("enter string: \n"))

# print(get_vowels(string))