# A basic reimplementation of some math functions in Python, namely
# Some statistical analysis and some calculations (if I'm lucky)
# Could just rename it as a terrible calculator, honestly
import matplotlib.pyplot as plt

# Global list variable
listofdata = []

# Ask the user for some data to input, append it to the global list
def promptfunction():
    answer = 0
    while (True):
        try:
            answer = float(input("Input an numeric value to the list of data you wish to preform statistics on (enter in a non-integer value to exit): "))
        except ValueError:
            break
        finally:
            listofdata.append(answer)

# Ask the user for a value, return the (float) value
def valueprompt():
    count = 0
    value =  input("Input a numeric value for the calculation to work on: ")
    if type(value) is str:
        for i in value:
            count += float(ord(i))
        return count
    else:
        return float(value)

# Ask the user for a value, return the (int) value
def intvalueprompt():
    count = 0
    value =  input("Input a numeric value for the calculation to work on: ")
    if type(value) is str:
        for i in value:
            count += int(ord(i))
        return count
    else:
        return int(value)
            
# Menu function, going to be a mammoth of a function
def menufunction():
    global listofdata # Call in the global variable 
    print("Hello, user! Please select an option:")
    choice = "Z"
    while(choice != "Q"):
        print("--------------------------------------------------------")
        print("Press 1 for Stats")
        print("Press 2 for Functional Calculations")
        print("Press Q for Quit")
        choice = input("Put choice here: ")
        if (choice == "1"):
            promptfunction()
            while(choice != 5):
                print("Now, choose a function to preform on the list of data you have entered:")
                print("Enter 1 for the average of the list")
                print("Enter 2 for the mode of the list")
                print("Enter 3 for the median of the list")
                print("Enter 4 to input another list")
                print("Enter 5 to return to the previous menu")
                choice = int(input())
                if (choice == 1):
                    print(averagelist(listofdata))
                elif (choice == 2):
                    print(mode(listofdata))
                elif (choice == 3):
                    print(medianlist(listofdata))
                elif (choice == 4):
                    listofdata = []
                    promptfunction()
                else:
                    if (choice != 5):
                        print("Invalid choice.")
        if (choice == "2"):
            while(choice != 4):
                print("Choose a function to use.")
                print("Enter 1 for a list of trigonometric functions")
                print("Enter 2 for a list of combinatoric functions")
                print("Enter 3 for fun-ctions")
                print("Enter 4 to return to the previous menu")
                choice = int(input())
                if (choice == 1):
                    while(choice != 4):
                        print("Choose something from the list of trigonemetric functions")
                        print("Enter 1 for the sine of a value")
                        print("Enter 2 for the cosine of a value")
                        print("Enter 3 for the tangent of a value")
                        print("Enter 4 to return to the previous menu")
                        choice = int(input())
                        if (choice == 1):
                            print(sine(valueprompt()))
                        if (choice == 2):
                            print(cosine(valueprompt()))
                        if (choice == 3):
                            print(tangent(valueprompt()))
                        if (choice == 4):
                            break
                        else:
                            if (choice != 4): # redundant? probably. but i am paranoid due to an above mistake
                                print("Invalid choice.")
                if (choice == 2):
                    while(choice != 3):
                        print("Choose something from the list of combinatoric functions:")
                        print("Enter 1 for the factorial of an integer")
                        print("Enter 2 for the n choose k of two integers")
                        print("Enter 3 to return to the previous menu")
                        choice = int(input())
                        if (choice == 1):
                            print(factorial(intvalueprompt()))
                        if (choice == 2):
                            print(nchoosek(intvalueprompt(), intvalueprompt()))
                        if (choice == 3):
                            break
                        else:
                            if (choice != 3):
                                print("Invalid choice.")
                            
    
                    
            
        


# Take the average of a VARIABLE LENGTH list
def averagelist(alist):
    asum = 0
    average = 0
    for i in alist:
        asum += i
    average = asum/(len(alist))
    return average

# Return the mean of a variable length list
def medianlist(alist):
    evenmedian = 0 # variable for median of an even list
    oddmedian = 0 # variable for median of an odd list
    if ((len(alist)%2) == 0):
        evenmedian = (alist[(len(alist)//2)] + alist[(len(alist)//2) - 1])/2
        # integer division floors, and we have an even number of data entries, so we add the two middle data points and divide by two
        return evenmedian
    else:
        oddmedian = float(alist[(len(alist)//2)]) # god i love it when i don't have to mess with indices, also matching datatypes
        return oddmedian

#implementing a sort algorithm for mode(alist)
def sort(alist):
    swap = 0
    for i in range(0, len(alist)):
        for x in range(0, i):
            if (alist[i] < alist[x]):
                swap = alist[i]
                alist[i] = alist[x]
                alist[x] = swap
    return alist

# Return the mode of a list
# Step 1: sort the list
# Step 2: count the numbers in the list
# Step 3: add counts of each number into another list
# Step 4: take maximum of final list
def mode(alist):
    mode = 0
    count = 1 # every item in a list appears at least once, lists should not be empty
    listcounts1 = listcounts(alist)
    listmodes = []
    maxcount = max(listcounts1)# this stores the amount of times the mode appears
    listsort = sort(alist) # sort the list before the algorithm

    # now we have to count throught the list again to convert the maxcount into an actual data value, which will be applied to the list of modes
    for i in range(0, len(listsort)):
        if ((i != (len(listsort)-1)) and (listsort[i] == listsort[i + 1])):
            count += 1
        elif (i == (len(listsort) - 1)):
            if(count == maxcount):
               listmodes.append(listsort[i])
        else:
            if(count == maxcount):
                listmodes.append(listsort[i])
            count = 1

    return listmodes

# function which takes in a list and returns a list of counts (component of the mode(alist) function and histogram(alist) function)
def listcounts(alist):
    listcounts = []
    count = 1 # every item in a list appears at least once, lists should not be empty
    listsort = sort(alist) # sort the list before the algorithm
    for i in range(0, len(listsort)):
        if ((i != (len(listsort)-1)) and (listsort[i] == listsort[i + 1])):
            count += 1
        elif (i == (len(listsort) - 1)): # woo messing with bounds
            listcounts.append(count)
        else:
            listcounts.append(count)
            count = 1
    return listcounts

# function which takes in an integer and returns its factorial
def factorial(n):
    factorialvar = 1
    for i in range(1, n+1):
        factorialvar *= i
    return factorialvar
# function which takes in a value and returns the sine of the value
def sine(value):
    value %= 2*3.14159265359 # truncating the value
    sine = value - ((value)**3/(factorial(3))) + ((value**5)/(factorial(5))) - ((value**7)/(factorial(7))) + ((value**9)/factorial(9))
    # error is x^11/11!, hardly anything to worry about
    return sine


# function which takes in a value and returns the cosine of the value
def cosine(value):
    value %= 2*3.1415925539 # truncating the value
    cosine = 1 - (value**2)/(factorial(2)) + ((value**4)/(factorial(4))) - ((value**6)/(factorial(6))) + ((value**8)/factorial(8)) - ((value**10/factorial(10)))
    # error is x^12/12!, hardly anything to worry about
    return cosine


# function which takes in a value and returns the tangent of the value
def tangent(value):
    value %= 2*3.1415925539
    return (sine(value)/cosine(value))

# function which takes in two integers and returns the n choose k of the two ints
def nchoosek(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))

# function which prints the first n rows of pascal's triangle
def pascalstriangle(n):
    for i in range(1, n+1):
        for x in range(1, i+1):
            print(nchoosek(i, x))

menufunction()
