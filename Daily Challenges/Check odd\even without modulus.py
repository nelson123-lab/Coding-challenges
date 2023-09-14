def odd_even(number):
    quotient = number/2
    if quotient == int(quotient): 
        return "even" 
    else:
        return "odd"

print(odd_even(111))
"""
odd
"""

"""
Here no modulus operator is used. When there is an even number, the number will be perfectly divisible by 2 and results in an integer number istead of float.
"""
