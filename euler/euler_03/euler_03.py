def largest_prime_factor(input):
    """600851475143"""
    divider = int(input ** 0.5)
    print divider
    while True:
        if input % divider == 0:
            print (divider)
            if is_prime(divider):
                return divider
        divider -= 1


def is_prime(prime_candidate):
    if prime_candidate % 2 != 0:
        for divider in xrange(3, int(prime_candidate ** 0.5)):
            if prime_candidate % divider == 0:
                print divider
                return False
        return True
    return False

# print largest_prime_factor(600851475143)
