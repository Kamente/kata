# Create a function named divisors/Divisors 
# that takes an integer n > 1 and returns an
# array with all of the integer's divisors(except 
# for 1 and the number itself), from smallest
# to largest. If the number is prime return the 
# string '(integer) is prime' (null in C#, empty
# table in COBOL) (use Either String a in Haskell
# and Result<Vec<u32>, String> in Rust).



def divisors(integer):
    if integer <= 1:
        return "Input should be greater than 1"
    
    divisors_list = []
    
    for divisor in range(2, integer):
        if integer % divisor == 0:
            divisors_list.append(divisor)
            
    if not divisors_list:
        return f"{integer} is prime"
    else:
        return divisors_list
    
print (divisors(12))
print (divisors(25))
print (divisors(13))