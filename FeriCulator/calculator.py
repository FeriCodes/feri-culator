import math

class Calculator:
    def __init__(self):
        pass
    
    def parse_and_validate(self, user_expr):
        """
        Parses and validates the user's input expression.
        Returns a tuple: (type, data)
        type can be 'back', 'error', 'sqrt', or 'calc'.
        data contains relevant info (number, operator, etc.) or an error message.
        """
        user_expr = user_expr.strip().lower()

        if user_expr in ["back", "b"]:
            return ("back", None)

        # Replace operators with spaces for easier splitting, ensuring spaces around them.
        operators = ["**", "//", "sqrt", "+", "-", "*", "/", "%"]
        for op in operators:
            user_expr = user_expr.replace(op, f" {op} ")

        user_expr = " ".join(user_expr.split())  # Remove extra spaces
        parts = user_expr.split()

        if not parts:
            return ("error", "Error: Please enter a calculation.")

        try:
            if parts[0] == "sqrt" and len(parts) == 2:
                n1 = float(parts[1])
                return ("sqrt", n1)

            elif len(parts) == 3:
                n1 = float(parts[0])
                op = parts[1]
                # Check if the operator is valid
                if op not in ["+", "-", "*", "/", "%", "**", "//"]:
                    return ("error", "Error: Invalid operator.")
                n2 = float(parts[2])
                return ("calc", (n1, op, n2))

            else:
                return ("error", "Error: Invalid format. Use 'num1 op num2' or 'sqrt num'")

        except ValueError:
            return ("error", "Error: Invalid number format.")
        except IndexError:
            return ("error", "Error: Missing operand or operator.")
        
    def calculate(self, num1, operator, num2=None):
        if operator == "sqrt":
            if num1 < 0:
                return "ERROR: Negative number for sqrt"
            return math.sqrt(num1)

        if num2 is None:
            return "ERROR: Missing second number"

        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "%":
            return num1 % num2 if num2 != 0 else "ERROR: Division by zero"
        elif operator == "//":
            return num1 // num2 if num2 != 0 else "ERROR: Division by zero"
        elif operator == "**":
            return num1**num2
        elif operator == "/":
            return num1 / num2 if num2 != 0 else "ERROR: Division by zero"
        else:
            return "ERROR: unknown operation!"