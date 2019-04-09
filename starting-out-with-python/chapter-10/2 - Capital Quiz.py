# A program which stores a list of states and their capitals in a dictionary,
# Then randomly quizzes the user on such things
dct1 = {'Arizona':'Phoenix', 'Alabama':'Montgomery', 'California':'Sacramento',
        'Washington':'Tacoma', 'Missouri':'St. Louis', 'Florida':'Tallahassee',
        'Georgia':'Atlanta'}
while dct1 != {}:
    state, capital = dct1.popitem()
    capin = input('What is the name of the capital of ' + str(state) + '? ')
    if capital == capin:
        print("Good job!")
    else:
        dct1[state] = capital
        print("You can try again...")
print('Congrats! You got them all correct!')
