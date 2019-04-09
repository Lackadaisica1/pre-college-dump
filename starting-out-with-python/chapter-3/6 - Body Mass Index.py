#A program to calculate BMI
def main():
    weight = float(input('What is your weight in pounds? '))
    height = float(input('What is your height in inches? '))
    BMI(weight, height)
def BMI(weight, height):
    BMI = (weight * 703) / (height ** 2)
    print('Here is your BMI: ', format(BMI, '.2f'))
main()
#Prevent prompt from closing:
input('Prompt lmao:')