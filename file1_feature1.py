def is_number(number):
    # Check if the input is an integer or a float
    return isinstance(number, int) or isinstance(number, float)

def division(numerator, denominator):
   # Raise an error if the denominator is 0
   if denominator == 0:
       raise ZeroDivisionError
   # Check if both inputs are numbers, otherwise raise a TypeError 
   if not is_number(numerator) and not is_number(denominator):
       raise TypeError
   # Perform the division if inputs are valid
   return numerator/denominator


