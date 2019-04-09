#A program which calculates the amount of cost for a paint job
def main():
    square_feet = float(input('How many square feet of wall will we paint today? '))
    price_paint = float(input('How many dollars will we spend per gallon of paint? '))
    calculate_everything_lmao(square_feet, price_paint)
def calculate_everything_lmao(square_feet, price_paint):
    req_paint = square_feet / 115
    labor_hours = (square_feet / 115) * 8
    tot_paint_cost = req_paint * price_paint
    labor_cost = 20 * labor_hours
    total_cost = tot_paint_cost + labor_cost
    print('Here is the gallons of paint required: ', format(req_paint, '.2f'))
    print('Here is the amount of hours required: ', format(labor_hours, '.2f'))
    print('Here is the amount of money the paint will cost: $', format(tot_paint_cost, '.2f'), sep='')
    print('Here is the amount of money the labor will cost: $', format(labor_cost, '.2f'), sep='')
    print('Here is the total cost of the job: $', format(total_cost, '.2f'), sep='')
main()
#Prevent prompt from closing
input('xd')