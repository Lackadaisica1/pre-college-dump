#A program to calculate how much minimum insurance people need
def main():
    cost_to_replace = float(input('How much do you need to replace the house? '))
    min_insurance(cost_to_replace)
def min_insurance(cost_to_replace):
    minimum = cost_to_replace * 0.8
    print('Here is the minimum insurance you need: $', format(minimum, ".2f"), sep='')
main()
#Prevent from closing
input('Prompt: ')