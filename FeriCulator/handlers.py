"""
This file handles the standard calculation and scientific calculation workflows.
"""


def handle_standard_calculator(standard_calc, history_tools):
    """
    1. Handles the standard calculator operations.
    """
    while True:
        user_input = input("Enter your calculation: ")
        result_type, data = standard_calc.parse_and_validate(user_input)
        if result_type == "back":
            break

        if result_type == "error":
            print(data)
            continue

        if result_type == "sqrt":
            n1 = data
            result = standard_calc.calculate_sqrt(n1)
            print(f"\nResult: {result}")

            if "ERROR" not in str(result):
                history_tools.save_calculation_to_history(f"sqrt {n1}", result)

        elif result_type == "calc":
            n1, op, n2 = data
            result = standard_calc.calculate(n1, op, n2)
            print(f"\nResult: {result}")

            if "ERROR" not in str(result):
                history_tools.save_calculation_to_history(f"{n1} {op} {n2}", result)


def handle_scientific_calculator(scientific_calc, history_tools):
    """
    2. Handles the scientific calculator operations.
    """
    while True:
        print("\n--- Scientific Calculator ---")
        print("Available operations: fac, sin, cos, tan, cot, pi")
        print("Type 'back' or 'b' to return to the main menu.")
        print("-" * 50)

        op = input("Enter operation: ").strip().lower()
        if op in ["back", "b"]:
            break

        if op not in ["fac", "sin", "cos", "tan", "cot", "pi"]:
            print("ERROR: Invalid Operation!")
            continue

        user_num = input("Enter number: ").strip()

        if user_num == "":
            if op == "pi":
                user_num = "1"
            else:
                print("ERROR: Number cannot be empty for this operation!")
                continue

        try:
            result = scientific_calc.calculate(op, user_num)
            print(f"\nResult: {result}")

            if "ERROR" not in str(result) and result != "Invalid Operation!":
                history_tools.save_calculation_to_history(f"{op} {user_num}", result)

        except ValueError:
            print("ERROR: Please enter a valid numeric value!")
        except (ZeroDivisionError, OverflowError) as e:
            print(f"Mathematical ERROR: {e}")
