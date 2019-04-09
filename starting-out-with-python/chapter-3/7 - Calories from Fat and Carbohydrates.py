#A program which will calculate the amount of calories gained from
#fat and carbohydrates
def main():
    calories_from_fat()
    calories_from_carbohydrates()
def calories_from_fat():
    grams_of_fat = float(input('How many grams of fat did you consume today? '))
    calories_of_fat = grams_of_fat * 9
    print('Here is the amount of fat calories you consumed today:', format(calories_of_fat, '.2f'))
def calories_from_carbohydrates():
    grams_of_carbohydrates = float(input('How many grams of carbohydrates did you consume today? '))
    calories_of_carbohydrates = grams_of_carbohydrates * 4
    print('Here is the amount of carbohydrate calories you consumed today:', format(calories_of_carbohydrates, '.2f'))
main()
#Prevent prompt from closing:
input('Prompt:')