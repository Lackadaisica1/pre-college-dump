# A program which encrypts a file by returning an encrypted list. Woo.
import pickle
codes = {'A':'&##', 'B':'@', 'C':'#', 'D':'$', 'E':'%', 'F':'^', 'G':'&))', 'H':'(', \
         'I':')', 'J':'=', 'L':'+', 'M':'-', 'N':'_', 'O':'{', 'P':'}', 'Q':'<', \
         'R':'>', 'S':'&^', 'T':'**', 'U':'`', 'V':'~', 'W':'///', 'X':'**', 'Y':'}}', \
         'Z':'=='}
filename = input('Input a file name to be encrypted (with .txt extension): ')
file = open(filename, 'r')
line_list = file.readlines()
encrypted_list = []
for lines in line_list:
    for ch in lines:
        if ch != '/' and ch != 'n' and ch.upper() in codes:
            encrypted_list.append(codes[ch.upper()])
        else:
            encrypted_list.append(ch)
file.close()
encrypted_file = open('encryptedfile.txt', 'wb')
pickle.dump(encrypted_list, encrypted_file)
encrypted_file.close()
