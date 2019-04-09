#A program to convert kilometers to miles
def main():
    kilometers = float(input('Enter the amount of kilometers: '))
    kilometers_meters(kilometers)
#Converting kilometers to miles
def kilometers_meters(kilometers):
    miles = 0.6284 * kilometers
    print('Here is the number of miles: ', miles)
#Call main()
main()
#Prevent prompt from closing
input("Don't close! ")
