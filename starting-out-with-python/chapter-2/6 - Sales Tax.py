#A program to calculate the amount of state and sales tax
#Ask the user for the purchase amount
purchase = float(input('How much did you spend today?: '))
#Calculate the sales tax, county tax, total tax, and total
county_tax = 0.02 * purchase
state_tax = 0.04 * purchase
total_tax = county_tax + state_tax
total = total_tax + purchase
#Print the amount of state tax, county tax, total, and total tax
print('The amount of state tax is: ', format(state_tax, ".2f"), '$')
print('The amount of county tax is: ', format(county_tax, ".2f"), '$')
print('The amount of total tax is: ', format(total_tax, ".2f"), '$')
print('The total is: ', format(total, ".2f"), '$')
#Prevent the prompt from closing
input('Prompt: ')
