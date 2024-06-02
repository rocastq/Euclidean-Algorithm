
# Create the class
class EuclideanAlgorithm:
    def __init__(self):
        pass
# Calculations to get the final result
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
            print('The value of "a" can not be greater than "b"')
            print('Try again')

#rename the class to make it more simple
euuclid = EuclideanAlgorithm

# Inputs
a = int(input('Give the first number (a): '))
b = int(input('Give the second number (b): '))

# Print the results with the given numbers
print(euuclid.calculate_gcd(a,b))
