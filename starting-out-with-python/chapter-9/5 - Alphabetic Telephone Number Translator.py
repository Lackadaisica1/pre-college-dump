# A program which translates an alphabetic telephone number and spits out the
# actual number
l_o_l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', \
                   'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', \
                   'W', 'X', 'Y', 'Z']
number = input('Enter an alphabetic phone number, seperated by dashes: ')
number = number.split('-')
first3 = number[0]
next3 = number[1]
last4 = number[2]
def letters_to_num(alphanum, l_o_l):
    alon = []
    for letter in alphanum:
        if letter in l_o_l[0:3]:
            number = 2
            alon.append(number)
        elif letter in l_o_l[3:6]:
            number = 3
            alon.append(number)
        elif letter in l_o_l[6:9]:
            number = 4
            alon.append(number)
        elif letter in l_o_l[9:12]:
            number = 5
            alon.append(number)
        elif letter in l_o_l[12:15]:
            number = 6
            alon.append(number)
        elif letter in l_o_l[15:19]:
            number = 7
            alon.append(number)
        elif letter in l_o_l[19:22]:
            number = 8
            alon.append(number)
        elif letter in l_o_l[22:]:
            number = 9
            alon.append(number)
    return alon
ihate = letters_to_num(first3, l_o_l)
my = letters_to_num(next3, l_o_l)
life = letters_to_num(last4, l_o_l)
def recombine(alon):
    recombine = ''
    for s in alon:
        recombine += str(s)
    return recombine
print(recombine(ihate) + '-' + recombine(my) + '-' + recombine(life))


