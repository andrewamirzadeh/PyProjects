#Author Name: Bijan Amirzadehasl
#Date: 09/04/2021
#Program Name: Amirzadehasl_Fahrenheit_to_Celsius.py
#Purpose: Prompt user to enter in a value and convert that value into celsius

#prompt user to enter the number that they wish to convert to celsius
#it is stored as a float and named farenheit
farenheit = float(input('Enter the Farenheit number you wish to convert to Celsius: '))


#algorithm named 'celsius' which is (f - 32) * 5 / 9
celsius = (farenheit - 32) * 5 / 9

#prints out a statement retrieving initial value the user entered and prints the conversion to celsius.
#calls the format function to bring celsius within two decimal places to read better
print("After conversion ", farenheit, " degrees converted to celsius is ", format(celsius, '.2f'))
