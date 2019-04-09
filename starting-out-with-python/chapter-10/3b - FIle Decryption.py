# A program to decrypt a file that you wrote in an encryption program. How fun.
import pickle
codes = {'&##':'A', '@':'B', '#':'C', '$':'D', '%':'E', '^':'F', '&))':'G', '(':'H', \
         ')':'I', '=':'J', '+':'L', '-':'M', '_':'N', '{':'O', '}':'P', '<':'Q', \
         '>':'Q', '&^':'R', '**':'S', '`':'T', '~':'U', '///':'W', '**':'X', '}}':'Y', \
         '==':'Z'}
import_file = open('encryptedfile.txt', 'rb')
emptylist = []
strings = ''
stringlist = []
encrypted_list = pickle.load(import_file)
for ch in encrypted_list:
    if ch in codes:
        emptylist.append(codes[ch])
    else:
        emptylist.append(ch)
import_file.close()
for ch in emptylist:
    if ch == '/n':
        stringlist.append(strings)
        strings = ''
    else:
        strings += ch
for line in stringlist:
    print(line)
print(encrypted_list)
print(emptylist)
