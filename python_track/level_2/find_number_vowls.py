def number_of_vowels  (string_data):
    vowels = {"a","e","i","o","u","A","E","I","O","U"} # set of all vowels considerin capital and small letters
    res = 0

    for s in string_data:
        res += (s in vowels) # counting number of vowels

    return res 

print(number_of_vowels("Abdul"))
