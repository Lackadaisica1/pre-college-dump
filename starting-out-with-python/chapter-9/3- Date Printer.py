# A program to read and print a date
date = input('What is the date today? (enter in mm/dd/yyyy format): ')
date = date.split('/')
monthi = date[0]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', \
          'October', 'November', 'December']
month = months[int(monthi) - 1]
day = date[1]
year = date[2]
print(month + ' ' + str(day) + ', ', str(year))
 
