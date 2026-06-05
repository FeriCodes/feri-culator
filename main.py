from FeriCulator.standard_calculator import Calculator
from FeriCulator.HistoryManager import History
from FeriCulator.scientific_calculator import ScientificCalculation


def show_menu():
    print("\n--- Main Menu ---")
    print("1. Standard Calculator")
    print("2. Scientifie Calculator")
    print("3. View History")
    print("4. Clear History")
    print("5. Help")
    print("6. Exit")
    print("\nEnter a calculation like: '5 + 3' or 'sqrt 16'")
    print("Type 'back' or 'b' to return to the main menu.")
    print("-" * 50)
    print()

    choice = input("Select an option (1-6): ")
    return choice


def view_help():  # 5 calculator help in the menu
    print("\n" + "-" * 30)
    print("      FeriCulator HELP")
    print("-" * 30)
    print("- Standard: 10 + 20 =")
    print("- Square Root: sqrt 144 =")
    print("- Supported: +, -, *, /, //, %, **, sqrt")
    print("- Type 'back' inside calculator to return to menu.")
    print("\nEnter a calculation like: '5 + 3' or 'sqrt 16'")
    print("Type 'back' or 'b' to return to the main menu.")
    print("-" * 30)
    input("\nPress Enter to return...")


def handle_exit():  # 6 exit the fericulate!
    print("Thank you for using Fericulator. Goodbye!")


def main():
    print("wellocme to the FeriCulator")
    standard_calc = Calculator()
    history_tools = History()
    scientific_calc = ScientificCalculation()
    while True:

        choice = show_menu()
        if choice == "1":
            while True:
                user_input = input("Enter your calculation: ")
                result_type, data = standard_calc.parse_and_validate(user_input)
                if result_type == "back":
                    break

                elif result_type == "error":
                    print(data)
                    continue

                elif result_type == "sqrt":
                    n1 = data

                    result = standard_calc.calculate(n1, "sqrt")
                    print(f"\nResult: {result}")

                    if "ERROR" not in str(result):
                        history_tools.save_calculation_to_history(f"sqrt {n1}", result)

                elif result_type == "calc":
                    n1, op, n2 = data
                    result = standard_calc.calculate(n1, op, n2)
                    print(f"\nResult: {result}")

                    if "ERROR" not in str(result):
                        history_tools.save_calculation_to_history(f"{n1} {op} {n2}", result)
    

        elif choice == "2":
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
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

        elif choice == "3":
            history_tools.view_history()
        elif choice == "4":
            history_tools.clear_history()
        elif choice == "5":
            view_help()
        elif choice == "6":
            handle_exit()
            break

        else:
            print("Invalid menu option. Please try again.")

if __name__ == "__main__":
    main()
