"""
Scientific calculator module for FeriCulator.
"""

import math


class ScientificCalculation:
    """
    Provides methods for performing scientific calculations such as factorial,
    trigonometric functions, and pi multiplication.
    """

    def __init__(self):
        pass

    def calculate_factorial(self, number):
        return math.factorial(number)

    def calculate_sin(self, degree):
        return math.sin(math.radians(degree))

    def calculate_cos(self, degree):
        return math.cos(math.radians(degree))

    def calculate_tan(self, degree):
        return math.tan(math.radians(degree))

    def calculate_cot(self, degree):
        return 1 / math.tan(math.radians(degree))

    def calculate_pi(self, number):
        return math.pi * number

    def calculate(self, operation, value):

        if operation == "fac":
            return self.calculate_factorial(int(value))

        if operation == "sin":
            return self.calculate_sin(float(value))

        if operation == "cos":
            return self.calculate_cos(float(value))

        if operation == "tan":
            return self.calculate_tan(float(value))

        if operation == "cot":
            return self.calculate_cot(float(value))

        if operation == "pi":
            return self.calculate_pi(float(value))

        return "Invalid Operation!"
