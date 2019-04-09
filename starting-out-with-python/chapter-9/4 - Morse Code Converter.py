# A program which converts a string into morse code
morse_list = [' ', '--..--', '.-.-.-', '..--..', '-----', '.----', '..---', \
              '...--', '....-', '.....', '-....', '--...', '---..', '----.', \
              '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', \
              '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', \
              '...', '-', '..-', '...-', '.--', '-..-', '-.-', '--..']
char_list = [' ', ',', '.', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', \
             '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', \
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
string = input('Input a string to be converted to morse code: ')
count = 0
print_list = []
def compare_char(char, count, print_list):
    if char.upper() == char_list[count]:
        morse = morse_list[count]
        print_list.append(morse)
    else:
        count += 1
        compare_char(char, count, print_list)
for ch in string:
    char = ch
    compare_char(char, count, print_list)
printstring = ''
for morse in print_list:
    printstring += morse + ' '
print(printstring)
