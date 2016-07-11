class MultiplesOf3And5(object):
    """If we list all the natural numbers below 10 that are multiples of 3 or 5,
     we get 3, 5, 6 and 9. The sum of these multiples is 23.

     Find the sum of all the multiples of 3 or 5 below 1000."""

    @staticmethod
    def get_n_numbers(param_number):
        numbers_array = []
        for number in xrange(1, param_number):
            numbers_array.append(number)
        return numbers_array

    def list_multiplies_of_3_and_5(self, boundary):
        multiples_of_3_and_5 = []
        for number_candidate in self.get_n_numbers(boundary):
            if self.is_multiple_of_3_or_5(number_candidate):
                multiples_of_3_and_5.append(number_candidate)
        return multiples_of_3_and_5

    @staticmethod
    def is_multiple_of_3_or_5(number):
        if number % 3 == 0 or number % 5 == 0:
            return number

    @classmethod
    def sum_array_of_numbers(cls, numbers):
        numbers_sum = 0
        for number in numbers:
            numbers_sum += number
        return numbers_sum
