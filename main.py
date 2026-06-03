from FeriCulator.calculator import Calculator
from FeriCulator.HistoryManager import History



def show_menu():
    print("\n--- Main Menu ---")
    print("1. Standard Calculator")
    print("2. View History")
    print("3. Clear History")
    print("4. Help")
    print("5. Exit")
    print("\nEnter a calculation like: '5 + 3' or 'sqrt 16'")
    print("Type 'back' or 'b' to return to the main menu.")
    print("-" * 50)
    print()
    choice = input("Select an option (1-5): ")
    return choice


def view_help():  # 4 calculator help in the menu
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


def handle_exit():  # 5 exit the fericulate!
    print("Thank you for using Fericulator. Goodbye!")


def main():
    print("wellocme to the FeriCulator")
    calc_tools = Calculator()
    history_tools = History()
    while True:

        choice = show_menu()
        if choice == "1":
            while True:
                user_input = input("Enter your calculation: ")
                result_type, data = calc_tools.parse_and_validate(user_input)
                if result_type == "back":
                    break

                elif result_type == "error":
                    print(data)
                    continue

                elif result_type == "sqrt":
                    n1 = data

                    result = calc_tools.calculate(n1, "sqrt")
                
                    
                    print(f"\nResult: {result}")

                    history_tools.save_calculation_to_history(f"{n1} {op} {n2}", result)

                elif result_type == "calc":
                    n1, op, n2 = data

                    result = calc_tools.calculate(n1, op, n2)
                    
                    print(f"\nResult: {result}")
                    history_tools.save_calculation_to_history(f"sqrt {n1}", result)
            
        elif choice == "2":
            history_tools.view_history()
        elif choice == "3":
            history_tools.clear_history()
        elif choice == "4":
            view_help()
        elif choice == "5":
            handle_exit()
            break

        else:
            print("Invalid menu option. Please try again.")

if __name__ == "__main__":
    main()
