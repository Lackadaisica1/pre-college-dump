#Ask the user for a temperature in Celsius
celsius = float(input('What is the temperature in Celsius?: '))
#Convert the temperature into Fahrenheit
fahrenheit = (9 / 5) * celsius + 32
#Display the temperature converted
print('Here is the temperature in Fahrenheit: ', format(fahrenheit, ".2f"))
#Prevent the prompt from closing
input('Prompt: ')