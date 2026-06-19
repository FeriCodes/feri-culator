"""
Scientific calculator module for FeriCulator.
"""

import math


class ScientificCalculation:
    """
    Provides methods for performing scientific calculations such as:
    factorial, trigonometric functions, square root, and pi multiplication.
    """

    def calculate_factorial(self, number: int):
        return math.factorial(number)

    def calculate_sin(self, degree: float):
        return math.sin(math.radians(degree))

    def calculate_cos(self, degree: float):
        return math.cos(math.radians(degree))

    def calculate_tan(self, degree: float):
        return math.tan(math.radians(degree))

    def calculate_cot(self, degree: float):
        try:
            return 1 / math.tan(math.radians(degree))
        except ZeroDivisionError:
            return "Math Error"

    def calculate_sqrt(self, number: float):
        if number < 0:
            return "Math Error"

        return math.sqrt(number)

    def calculate_pi(self, number=None):
        if number is None:
            return math.pi

        return math.pi * number

    def calculate_log(self, number: float):
        if number <= 0:
            return "Math Error"
        return math.log10(number)

    def calculate(self, operation: str, value):
        """
        Dispatch scientific calculations based on operation name.

        Supported operations:
        - fac
        - sin
        - cos
        - tan
        - cot
        - sqrt
        - log
        - pi
        """

        try:
            value = float(value)

            if operation == "fac":
                if value < 0 or not value.is_integer():
                    return "Math Error"

                return self.calculate_factorial(int(value))

            if operation == "sin":
                return self.calculate_sin(value)

            if operation == "cos":
                return self.calculate_cos(value)

            if operation == "tan":
                return self.calculate_tan(value)

            if operation == "cot":
                return self.calculate_cot(value)

            if operation == "sqrt":
                return self.calculate_sqrt(value)

            if operation == "log":
                return self.calculate_log(value)

            if operation == "pi":
                return self.calculate_pi(value)

            return "Invalid Operation!"

        except (ValueError, TypeError):
            return "Math Error"
