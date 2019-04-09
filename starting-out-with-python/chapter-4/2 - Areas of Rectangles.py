#A program which asks for the length and width of two rectangles,
#Calculates the area of both, and compares the areas of the two.
def main():
    #Get the width and length for both of the rectangles
    width1 = float(input('What is the width of the first rectangle? '))
    length1 = float(input('What is the length of the first rectangle? '))
    width2 = float(input('What is the width of the second rectangle? '))
    length2 = float(input('What is the length of the second rectangle? '))
    calculate_area(width1, length1, width2, length2)
#A program to calculate the area of the rectangles and compare them
def calculate_area(width1, length1, width2, length2):
    area1 = width1 * length1
    area2 = width2 * length2
    if area1 > area2:
        print('The area of the first rectangle is greater than the area of the second.')
    elif area1 == area2:
        print('The area of the rectangles are equal.')
    else:
        print('The area of the second rectangle is greater than the area of the first.')
#Call the function
main()
#Prevent the prompt from closing:
input('lmao ')
