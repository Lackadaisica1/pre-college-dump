#A program to calculate automobile costs
def main():
    loan_payment = float(input('How much do you pay monthly for your loan? '))
    insurance = float(input('How much do you pay monthly for insurance? '))
    gas = float(input('How much do you pay monthly for gas? '))
    maitnence = float(input('How much do you pay monthly for maitnence? '))
    calc_auto(loan_payment, insurance, gas, maitnence)
#Actual calculations
def calc_auto(loan_payment, insurance, gas, maitnence):
    total_monthly_payment = loan_payment + insurance + gas + maitnence
    total_annual_payment = loan_payment * 12 + insurance * 12 + gas * 12 + maitnence * 12
    print('Here is your total monthly expense for the car: $', format(total_monthly_payment, ".2f"), sep='')
    print('Here is your total annual expense for the car: $', format(total_annual_payment, ".2f"), sep='')
main()
#Prevent prompt from closing
input('Prompt: ')