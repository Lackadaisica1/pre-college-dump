# A program that stores every unique word in a list and displays them in a set
filename = input('Input a file name (with .txt extension): ')
file = open(filename, 'r')
line_list = []
word_list = []
for line in file:
    line_list.append((line.rstrip()))
for line in line_list:
    line1 = line.split(' ')
    for word in line1:
        word_list.append(word)
myset = set(word_list)
print(myset)

