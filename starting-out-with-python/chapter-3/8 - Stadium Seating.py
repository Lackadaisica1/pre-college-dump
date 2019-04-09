#A program which calculates the income from Stadium Seating
def main():
    classa = float(input('How many seats were sold in the Class A category?: '))
    classb = float(input('How many seats were sold in the Class B category?: '))
    classc = float(input('How many seats were sold in the Class C category?: '))
    seating(classa, classb, classc)
def seating(classa, classb, classc):
    incomea = 15 * classa
    incomeb = 12 * classb
    incomec = 9 * classc
    total_income = incomea + incomeb + incomec
    print('Here is your total income: $', format(total_income, ".2f"), sep='')
main()
#Prevent prompt from closing
input('xd')