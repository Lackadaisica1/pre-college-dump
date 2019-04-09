# A program designed to get first, middle, and last initials from a name
first_name = input('What is your first name? ')
middle_name = input('What is your middle name? ')
last_name = input('What is your last name? ')
initials = first_name[0] + '.' + middle_name[0] + '.' + last_name[0]
print(initials)
