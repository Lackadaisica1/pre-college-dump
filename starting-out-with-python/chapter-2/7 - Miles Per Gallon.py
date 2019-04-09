#Ask the user for miles driven and gallons of gas used
miles_driven = float(input('How many miles have you driven?: '))
gallons_of_gas = float(input('How many gallons of gas have you used?: '))
#Calculate the MPG and display the result
MPG = miles_driven / gallons_of_gas
print('Here is your miles per gallon: ', format(MPG, ".2f"))
#Prevent prompt from closing
input('Prompt: ')
