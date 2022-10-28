
'''
this is used to rule out the errors coming by using an exception by y=using the except fn.
first it tries the code and if it is invalid or error it goes to the except op and executes the except code.
'''

try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input!!!")

try:
    value = 10/0
    num = float(input("Enter the number: "))
    print(num)
except ZeroDivisionError as err:
    print(err)
except ValueError as ve:
    print(ve)