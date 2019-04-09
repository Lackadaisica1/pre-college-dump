#A program which calculates the monthly sales tax for something i dunno dood
def main():
    total_sales = float(input('What are your sales for the month?: '))
    calculate_sales(total_sales)
def calculate_sales(total_sales):
    county_tax = total_sales * 0.02
    state_tax = total_sales * 0.04
    total_tax = state_tax + county_tax
    print('Here is the amount of county sales tax: $', format(county_tax, '.2f'), sep='')
    print('Here is the amount of state tax: $', format(state_tax, '.2f'), sep='')
    print('Here is the amount of total sales tax: $', format(total_tax, '.2f'), sep='')
main()
#Prevent the prompt from closing
input('xd')