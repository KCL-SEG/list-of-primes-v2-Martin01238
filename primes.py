"""values of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <=0:
        raise ValueError("No <= 0 values.")
    values = []
    initial = 2
    while len(values) < number_of_primes:
        pcheck = [initial for i in values if initial%i == 0]
        values += [] if pcheck else [initial]
        initial += 1
    return values