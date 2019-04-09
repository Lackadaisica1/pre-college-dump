# A function that counts vowels and consonants in a string, what joy!
def consonantf(string):
    count = 0
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o',
                  'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    for ch in string:
        if ch in consonants:
            count += 1
    return count
def vowelf(string):
    count = 0
    vowel = ['a', 'e', 'i', 'o', 'u']
    for ch in string:
        if ch in vowel:
            count += 1
    return count
string = input('Input a string to have stuff counted lol ')
ccount = consonantf(string)
vcount = vowelf(string)
print('Here is the number of consonants:', ccount)
print('Here is the number of vowels:', vcount)
