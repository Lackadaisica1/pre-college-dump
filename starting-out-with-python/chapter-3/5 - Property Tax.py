#A program to calculate the amount of property taxes on a property
def main():
    property_value = float(input('How much is your property worth? '))
    assessment_value = 0.60 * property_value
    property_tax = (assessment_value / 100) * 0.64
    print('Here is the assessment value of your property: $', format(assessment_value, '.2f'), sep='')
    print('Here is the property tax levied on your property: $', format(property_tax, '.2f'), sep='')
main()
#Prevent prompt from closing:
input('Prompt lmao:' )
