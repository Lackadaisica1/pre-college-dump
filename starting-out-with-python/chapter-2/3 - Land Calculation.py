#Ask the user for the number of feet in the tract:
total_square_feet = int(input('Amount of feet in tract: ' ))
#Divide the amount of feet by 43560 to get acres
acres = format(total_square_feet / 43560, ".2f")
#Display the amount of acres
print('Your land contains', acres, 'acres')
#Prevent closing
input("Prompt: ")
