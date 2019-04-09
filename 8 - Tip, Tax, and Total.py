#Ask the user for the food amount:
amount_paid = float(input('How much did you pay for the food? '))
#Calculate the amount of the tip, total and the sales tax:
tip = 0.15 * amount_paid
sales_tax = 0.07 * amount_paid
total = amount_paid + tip + sales_tax
#Display the tip, total, and sales_tax
print('Here is your tip paid: ', format(tip, ".2f"), '$')
print('Here is your amount of sales tax paid: ', format(sales_tax, ".2f"), '$')
print('Here is your total: ', format(total, ".2f"), '$')
#Prevent the prompt from closing
input('Prompt: ')