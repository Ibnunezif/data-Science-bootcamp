def number_of_vowels  (string_data):
    vowels = {"a","e","i","o","u","A","E","I","O","U"} # set of all vowels considerin capital and small letters
    res = 0

    for s in string_data:
        res += (s in vowels) # counting number of vowels

    return res 

while True:
    print("Give me string that you want to count te vowels for:")
    s = input()
    print(f"Number of vowels in string is = {number_of_vowels(s)}")
