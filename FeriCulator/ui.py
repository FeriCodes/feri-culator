"""Simple UI for Fericulator."""


def show_menu():
    """
    Displays the main menu and prompts the user for a choice.
    """
    while True:
        print("\nWelcome to the FeriCulator\n")
        print("\n--- Main Menu ---")
        print("1. Standard Calculator")
        print("2. Scientific Calculator")
        print("3. View History")
        print("4. Clear History")
        print("5. Help")
        print("6. Exit")
        print("\nEnter a calculation like: '5 + 3' or 'sqrt 16'")
        print("Type 'back' or 'b' to return to the main menu.")
        print("-" * 50)
        print()

        choice = input("Select an option (1-6): ")
        if choice in ["1", "2", "3", "4", "5", "6"]:
            return choice

        print("\n❌ Invalid choice! Please enter a number between 1 and 6.")
        print("Let's try again...")


def view_help():
    """
    5. Displays help information about how to use the calculator.
    """
    print("\n" + "-" * 30)
    print("      FeriCulator HELP")
    print("-" * 30)
    print("- Standard: 10 + 20 =")
    print("- Square Root: sqrt 144 =")
    print("- Supported: +, -, *, /, //, %, **, sqrt")
    print("- Type 'back' inside calculator to return to menu.")
    print("\nEnter a calculation like: '5 + 3' or 'sqrt 16'")
    print("Type 'back' or 'b' to return to the main menu.")
    print("\nScientific Operations:")
    print("- Factorial: fac 5")
    print("- Sine: sin 30")
    print("- Supported: fac, sin, cos, tan, cot, pi")
    print("- Type 'back' inside calculator to return to menu.")
    print("-" * 30)
    input("\nPress Enter to return...")


def handle_exit():
    """
    6. Exits the application gracefully.
    """
    print("Thank you for using Fericulator. Goodbye!")
