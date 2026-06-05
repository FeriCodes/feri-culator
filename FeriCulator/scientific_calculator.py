import math

class ScientificCalculation:
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
            
        elif operation == "sin":
            return self.calculate_sin(float(value))
            
        elif operation == "cos":
            return self.calculate_cos(float(value))
            
        elif operation == "tan":
            return self.calculate_tan(float(value))
            
        elif operation == "cot":
            return self.calculate_cot(float(value))
            
        elif operation == "pi":
            return self.calculate_pi(float(value))
            
        else:
            return "Invalid Operation!"