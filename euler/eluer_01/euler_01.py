class MultiplesOf3And5(object):
    """If we list all the natural numbers below 10 that are multiples of 3 or 5,
     we get 3, 5, 6 and 9. The sum of these multiples is 23.

     Find the sum of all the multiples of 3 or 5 below 1000."""

    def get_n_numbers(self, param_number):
        numbers_array = []
        for number in xrange(1, param_number+1):
            numbers_array.append(number)
        return numbers_array

    def is_multiple_of_3(self, number):
        if number % 3 == 0:
            return True
        return False
