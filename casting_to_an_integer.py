"""
Program: cast_to_an_integer.py
Author: Cody Kelderman
Last date modified: 8/23/23
The purpose of this program is to accept any input,
convert to a integer type and output the integer.
"""
def integer_converter(num):
    new_number = int(num)
    print(new_number)

integer_converter(2.33)
integer_converter(4.5)
integer_converter(4.51)
integer_converter(-4.51)
integer_converter('110')
integer_converter('pickle')

# Input         Expected Output               Actual Output
#    2.33             2                       2
#    4.5              4                       4
#    4.51             5                       4
#    -4.51           -4                       4
#    '110'            110                     110
#    'pickle'         type error              valuError: invalid literal for int() with base 10: 'pickle'