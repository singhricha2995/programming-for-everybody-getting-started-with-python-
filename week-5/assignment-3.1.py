#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

h=input('Enter the hours:')
r=input('Enter the rate:')
hrs = float(h)
rte = float(r)
if hrs<=40:
    print(hrs*rte)
if hrs>40:
    print(40*rte+(hrs-40)*rte*1.5)

        
