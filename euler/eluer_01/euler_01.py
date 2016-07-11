class MultiplesOf3And5(object):

    def multiples_of_3_and_5(self, border):
        result = 0
        for number in range(1, border):
            if number % 3 == 0 or number % 5 == 0:
                result += number
        return result
