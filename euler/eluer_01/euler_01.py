class MultiplesOf3And5(object):
    """If we list all the natural numbers below 10 that are multiples of 3 or 5,
     we get 3, 5, 6 and 9. The sum of these multiples is 23.

     Find the sum of all the multiples of 3 or 5 below 1000."""

    def get_n_numbers(self, param_number):
        numbers_array = []
        for number in xrange(1, param_number):
            numbers_array.append(number)
        return numbers_array

    def is_multiple_of_3(self, number):
        if number % 3 == 0:
            return True
        return False

    def is_multiple_of_5(self, number):
        if number % 5 == 0:
            return True
        return False

    def list_multiplies_of_3_and_5(self, boundary):
        multiples_of_3_and_5 = []
        for number_candidate in self.get_n_numbers(boundary):
            if self.is_multiple_of_3(number_candidate) \
                    or self.is_multiple_of_5(number_candidate):
                multiples_of_3_and_5.append(number_candidate)
        return multiples_of_3_and_5
