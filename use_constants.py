"""
Program: use_constants.py
Author: Cody Kelderman
Last date modified: 08/23/23
The purpose of this program is to take different variables and present them as a unified string.
"""

# get variable value from constant.py (this proved troublesome with simply the 'import' command)
from constant import PRICE_OF_HATS

# define variables
quantity = 2
item = "hat"
size = 7.0

# display in terminal
print(type(quantity))
print(type(item))
print(type(size))
print(PRICE_OF_HATS)

# takes variable data and prints a string which changes upon different entries
def first_program(amount, type, bigness):
    if amount == 1:
        print(str(amount) + " " + type + " size " + str(bigness) + " costs $" + str(PRICE_OF_HATS))
    elif amount == 0:
        print("No hats for you")
    elif amount < 0:
        print("I don't owe you anything")
    else:
        print(str(amount) + " " + type + "s size " + str(bigness) + " cost $" + str((PRICE_OF_HATS)* amount))

first_program(quantity, item, size)