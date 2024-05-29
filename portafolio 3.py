
# Create the class
class EuclideanAlgorithm:
    def __init__(self):
        pass

    def calculate_gcd(a, b):
        """
     EuclideanAlgorithm(a, b)
    While b is not equal to 0
        temp = b
        b = a mod b
        a = temp
    Return a
        """
        if a > b:
            while b != 0:
                temp = b
                b = a % b
                a = temp
            return a
# Give an error message if the digits are not the ones that we need.
        else:
            print('error')

#rename the class to make it more simple
euuclid = EuclideanAlgorithm

print(euuclid.calculate_gcd(293,173))
