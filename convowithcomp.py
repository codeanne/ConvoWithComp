print ('Hello World!') #Says Hello
print('What is your name?') #Asks the user their name.
yourName = input() #assignment statement for name variable
print ('It is nice to meet you ' + yourName) #1st resuse of a user input

print ('How are you today?') #Asks the user how they are feeling
mood = input() #assignment statement for mood variable
print ('What a coincidence, I am also feeling ' + mood) #2nd reuse of a user input

print ('How old are you?') #Asks the user for their age
age = input() #assignment statement for age variable
print (age + ' is a great age to be') #3rd reuse of a user input

print ('What year is it now?') #Asks for the current year
year = input() #assignment statement for year variable
print ('Then next year, it will be ' + str(int(year)+ 1)) #Type convert integer into a string to concatenate
#Does simple plus one arithmetic to the year input value

input('Enter any key to close the program.') #To prevent the python cmd prompt from closing immediately after last input
