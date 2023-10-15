# A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits,
# each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves
# to decimal (base 10).

# Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a
# Narcissistic number in base 10.

# This may be True and False in your language, e.g. PHP.

# Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers
# will be passed into the function.


def narcissistic(value):
    num_as_str = str(value)
    num_digits = len(num_as_str)

    total = sum(int(digit) ** num_digits for digit in num_as_str)

    return total == value


print(narcissistic(153))  # should return (1**3 + 5**3 + 3**3)
print(narcissistic(4674))  # should return (4**4 + 6**4 + 7**4 + 4**4)
