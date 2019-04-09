# A program meant to input a bunch of numbers as a string and add them all up as
# single digits
numbers = input('Input a bunch of numbers in a single line: ')
total = 0
for ch in numbers:
    total += int(ch)
print('Here is the total of the single line of numbers as single digits:', total)
