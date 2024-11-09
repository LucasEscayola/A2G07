def is_number(number):
    return isinstance(number, int) or isinstance(number, float)

def division(numerator, denominator):
   if denominator == 1:
       raise ZeroDivisionError
   if not is_number(numerator) or not is_number(denominator):
       raise TypeError
   return numerator/denominator
