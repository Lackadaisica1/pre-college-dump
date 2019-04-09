#A program to calculate the weight of an object's mass and compare it
#to 1000 and 10 Newtons
def main():
    mass = float(input('How much is the mass of the object? '))
    weight_calc(mass)
def weight_calc(mass):
    weight = 9.8 * mass
    if weight > 1000:
        print('The object weighs too much!')
    elif weight < 10:
        print('The object weighs too little!')
    else:
        print("Here is the object's weight in Newtons: ", format(weight, '.2f'))
#Call the function
main()
#Prevent the prompt from closing
input('lmao ')