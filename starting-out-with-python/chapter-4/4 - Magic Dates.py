#A program to see whether a date is 'magic' or not
def main():
    month = int(input('Input a number, 1-12, which represents the month: '))
    day = int(input('Input a number, 1-30/31, which represents the day: '))
    year = int(input('Input the last two digits of the year: '))
    magic_date(month, day, year)
def magic_date(month, day, year):
    if month * day == year:
        print('This is a magic date!')
    else:
        print("This's a not magic date.")
#Call the function
main()
#Prevent prompt from closing
input('lmao ')