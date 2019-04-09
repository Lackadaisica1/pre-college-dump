# A program which reads the contents of two text files and compares them
# To use a bunch of set functions lol
filename1 = input('What is the filename of the first file (with .txt extension)? ')
filename2 = input('What is the filename of the second file (with .txt extension)? ')
file1 = open(filename1, 'r')
file2 = open(filename2, 'r')
listlines1 = file1.readlines()
listlines2 = file2.readlines()
file1.close()
file2.close()
list1 = []
list2 = []
for stuff in listlines1:
    stuff = stuff.rstrip('\n')
    stuff = stuff.split(' ')
    list1.append(stuff)
for stuff in listlines2:
    stuff = stuff.rstrip('\n')
    stuff = stuff.split(' ')
    list2.append(stuff)
wordlist1 = []
wordlist2 = []
for stuff in list1:
    for word in stuff:
        wordlist1.append(stuff)
for stuff in list2:
    for word in stuff:
        wordlist2.append(stuff)
set1 = set()
set2 = set()
for stuff in wordlist1:
    set1.update(stuff)
for stuff in wordlist2:
    set2.update(stuff)
union = set1.union(set2)
intersection = set1.intersection(set2)
wordlist1diff = set1 - set2
wordlist2diff = set2 - set1
symdiff = set1.symmetric_difference(set2)
print('Here is the union of the words in both files: ', union)
print('Here is the intersection of the words in both files: ', intersection)
print('Here is the difference between file 1 and file 2 words: ', wordlist1diff)
print('Here is the difference between file 2 and file 1 words: ', wordlist2diff)
print('Here is the symmetric difference between the sets: ', symdiff)
