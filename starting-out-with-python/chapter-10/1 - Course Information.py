# A program which creates three dictionaries and displays course room number,
# instructor, and meeting time
dct1 = {'CS101':3004, 'CS102':4501, 'CS103':6755, 'NT110':1244, 'CM241':1411}
dct2 = {'CS101':'Haynes', 'CS102':'Alvarado', 'CS103':'Rich', 'NT110':'Burke', \
        'CM241':'Lee'}
dct3 = {'CS101':'8:00 a.m.', 'CS102':'9:00 a.m.', 'CS103':'10:00 a.m.', \
        'NT110':'11:00 a.m.', 'CM241':'1:00 p.m.'}
key = input('Input the course number you would like to search for from the dictionary: ')
print('Here is the room number:', dct1[key])
print('Here is the instructor:', dct2[key])
print('Here is the meeting time:', dct3[key])
