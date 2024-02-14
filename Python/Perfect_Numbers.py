def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number > 0:
        perfect_number = sum([x for x in range(1, number) if number % x == 0])
        if perfect_number == number:
            return "perfect"
        if perfect_number > number:
            return "abundant"
        if perfect_number < number:
            return "deficient"
    
    raise ValueError("Classification is only possible for positive integers.")
