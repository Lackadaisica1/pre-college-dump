# A program that stores 20 numbers in a list and then displays the total of the
# Numbers in the list, the lowest number in the list, and the highest number
# In the list
def main():
    list1 = number_list()
    max_min_list(list1)
    total = total_list(list1)
    average_list(total)
# A function used to ask the user what numbers fit in the list
def number_list():
    list1 = []
    for i in range(20):
        number = input('Hey, input a number to a list! ')
        list1.append(number)
    return list1
# A function used to calculate and display the maximum of list1
def max_min_list(list1):
    maximum = max(list1)
    print('Here is the maximum of the list of values:', maximum)
    minimum = min(list1)
    print('Here is the minimum of the list of values:', minimum)
# A function used to calculate and display the total of list1
def total_list(list1):
    total = 0
    for number in list1:
        total += int(number)
    return total
    print('Here is the total of the values in the list,', total)
# A function used to calculate and display the average of the list
def average_list(total):
    average = total / 20
    print('Here is the average of the list:', average)
main()
    
