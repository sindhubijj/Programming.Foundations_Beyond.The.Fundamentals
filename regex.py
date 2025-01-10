#REGUALAR EXPRESSION INTRODUCTION
import re

#Declaring Variables 
five_digit_zip = '98101' 
nine_digit_zip = '98101-0003'
phone_number = '234-567-8901'

five_digit_expression = r'\d{5}' #create a variable

print(re.search(five_digit_expression, five_digit_zip)) 
    #comparing the 5 digit expression with 5 digit zip code
print(re.search(five_digit_expression, nine_digit_zip))
    #comparing the 5 digit expression with the 9 digit zip code
print(re.search(five_digit_expression, phone_number))
    #comparing the 5 digit expression with the phone number 
