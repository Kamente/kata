def narcissistic(value):
    num_as_str = str(value)
    num_digits = len(num_as_str)
    
    total = sum(int(digit) ** num_digits for digit in num_as_str)
    
    return total == value

print(narcissistic(153))
print(narcissistic(46754))