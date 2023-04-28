# Credit_Checker


This program checks if a credit card number is valid or not. It uses the Luhn algorithm to validate the credit card number.

Requirements
Python 3.0 or higher
How to Use:
Open the terminal or command prompt.
Navigate to the directory where the program file is located.
Run the program using the following command: python credit_card_validator.py
Enter the credit card number when prompted.
The program will output whether the credit card number is valid or not.
Note: The program only accepts numeric input. Do not include any spaces or other non-numeric characters in the credit card number.

Algorithm:
The program uses the Luhn algorithm to validate the credit card number. The algorithm works as follows:

Starting from the rightmost digit, double every second digit.
If the result of doubling a digit is greater than 9, add the two digits together to get a single-digit number.
Sum all the digits.
If the total sum is divisible by 10, the credit card number is valid.
