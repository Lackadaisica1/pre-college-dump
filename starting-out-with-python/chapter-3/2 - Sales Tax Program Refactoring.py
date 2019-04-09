#A program to calculate sales tax (Copied from 2-6)
def main():
    purchase = float(input('Enter amount purchased: '))
    calculations(purchase)
def calculations(purchase):
    county_tax = 0.02 * purchase
    state_tax = 0.04 * purchase
    total_tax = 0.04 * purchase + 0.02 * purchase
    total = purchase + 0.04 * purchase + 0.02 * purchase
    print('The amount of state tax is: ', format(state_tax, ".2f"), '$')
    print('The amount of county tax is: ', format(county_tax, ".2f"), '$')
    print('The amount of total tax is: ', format(total_tax, ".2f"), '$')
    print('The total is: ', format(total, ".2f"), '$')
#Call main
main()
#Prevent the prompt from closing
input('Prompt: ')
