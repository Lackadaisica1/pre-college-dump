#Ask the user to input the price of each item
item1 = float(input('Enter the price of the first item: '))
item2 = float(input('Enter the price of the second item: '))
item3 = float(input('Enter the price of the third item: '))
item4 = float(input('Enter the price of the fourth item: '))
item5 = float(input('Enter the price of the fifth item: '))
#Add up the prices of the items to get the subtotal
subtotal = item1 + item2 + item3 + item4 + item5
#Calculate the price of the sales tax
sales_tax = 0.06 * subtotal
#Calculate the total
total = subtotal + sales_tax
#Display the subtotal, sales tax, and total
print('The subtotal is: ', (format(subtotal, '.2f')), '$')
print('The sales tax is: ', (format(sales_tax, '.2f')), '$')
print('The total is: ', (format(total, '.2f')), '$')
#Prevent the prompt from closing
input('Prompt: ')