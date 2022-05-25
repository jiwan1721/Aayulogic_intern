from vowels import get_vowels

def test_vowel():
    string = "my name is lakhan"
    test = get_vowels(string)
    assert ['a','e','i','a','a'] == test,'error in functin'
    
test_vowel()