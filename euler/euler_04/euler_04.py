def palindromic_number():
    """A palindromic number reads the same both ways.
    The largest palindrome made from the product of
    two 2-digit numbers is 9009 = 91 * 99.

    Find the largest palindrome made from the product
    of two 3-digit numbers."""
    num1 = 999
    num2 = 999
    palindrome_numbers = []
    while True:
        num = num1 * num2
        if is_palindromic(num):
            palindrome_numbers.append(num)
        else:
            if num2 < 900:
                return sorted(palindrome_numbers)
            elif num1 == num2:
                num1 -= 1
            elif num1 == 900:
                num1 = 999
                num2 -= 1


def is_palindromic(number):
    number_as_string = str(number)
    number_length = number_as_string.__len__()
    new_string = ''
    for field in range(1, number_length+1):
        new_string += number_as_string[-field]
    if new_string == number_as_string:
        return True
    return False


print palindromic_number()
