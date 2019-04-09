# A program which stores a bunch of words and counts the numbers of times
# They appear. Like, as a frequency
filename = input('What is the file name (with text extension): ')
file = open(filename, 'r')
line_list = file.readlines()
file.close()
word_list = []
for line in line_list:
    line = line.rstrip()
    line = line.rstrip('.')
    line = line.rstrip(',')
    line = line.split(' ')
    word_list.append(line)
worddct = {}
for phrase in word_list:
    for word in phrase:
        if word not in worddct:
            worddct[word] = 1
        else:
            worddct[word] += 1
print(worddct)
