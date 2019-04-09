#Calculate the amount of money, the comission, and the amount left
#As Joe bought the stock
amount_paid = 1000 * 32.87
commission_paid_paid = 0.02 * amount_paid
amount_sold = 1000 * 33.92
commission_paid_sold = 0.02 * amount_sold
joe_profit = amount_sold - commission_paid_paid - commission_paid_sold - amount_paid
#Display the amounts of money paid and sold, the commission, and the profit
#for Joe
print('Here is the amount paid for the stock: ', format(amount_paid, ".2f"), '$')
print('Here is the amount gained from the stock: ', format(amount_sold, ".2f"), '$')
print('Here is the amount given to the commissioner when the stock was bought: ', format(commission_paid_paid, ".2f"), '$')
print('Here is the amount given to the commissioner when the stock was sold: ', format(commission_paid_sold, ".2f"), '$')
print('Here is your profit: ', format(joe_profit, ".2f"), '$')
#Prevent the prompt from closing
input('Prompt: ')
