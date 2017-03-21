"""
-----------------------------------------------------------------------
Question 1.

Given two int values, return True if one is negative and one is
positive. Except if the parameter "negative" is True, then return True
only if both are negative.
-----------------------------------------------------------------------

"""


def pos_neg(a, b, negative):

    n = negative
    if negative is True:
        n1 = 1
    else:
        n1 = 0


    if a > 0 and b < 0:
        return 'true'

    elif a < 0 and b > 0:
        return 'true'

    elif a < 0 and n1 == 1 and b < 0:
            return 'true'

    else:
        return 'false'



# Expected outputs:

print(pos_neg(1, -1, False))
# True
print(pos_neg(-1, 1, False))
# True
print(pos_neg(-4, -5, True))
# True
print(pos_neg(-2, -5, False))
# False
print(pos_neg(1, 2, False))
# False


"""
-----------------------------------------------------------------------
Question 2.

A year with 366 days is called a leap year. Leap years are necessary to
keep the calendar synchronized with the sun because the earth revolves
around the sun once every 365.25 days. Actually, that figure is not
entirely precise, and for all dates after 1582 the Gregorian correction
applies. Usually years that are divisible by 4 are leap years, for
example 1996. However, years that are divisible by 100 (for example,
1900) are not leap years, but years that are divisible by 400 are leap
years (for example, 2000).
-----------------------------------------------------------------------

"""


def leap_year(year):

    y_4 = year/4
    y_100 = year/100
    y_400 = year/400

    ex = (year % 100 == 0 and year % 400 != 0)




    if year % 4 == 0 and ex is False:
        return 'leap-year'
    else:
        return 'nope not this year!'


# When you've completed your function, uncomment the
# following lines and run this file to test!

print(leap_year(1900))
print(leap_year(2016))
print(leap_year(2017))
print(leap_year(2000))




"""
-----------------------------------------------------------------------
Question 3:

Write a function with loops that computes the sum of all squares between
1 and n (inclusive).
-----------------------------------------------------------------------

"""

import math

def sum_squares(n):

   return sum([i**2 for i in range(1, n+1)])


# When you've completed your function, uncomment the
# following lines and run this file to test!

print(sum_squares(1))
print(sum_squares(100))
