"""
FeriCulator: A scientific calculator with history management.
Main entry point of the application.
"""

from FeriCulator.standard_calculator import Calculator
from FeriCulator.history_manager import History
from FeriCulator.scientific_calculator import ScientificCalculation
from FeriCulator.ui import show_menu, view_help, handle_exit
from FeriCulator.handlers import (
    handle_standard_calculator,
    handle_scientific_calculator,
)


def main():
    """
    Displays a welcome message and the main menu.
    Handles user input to navigate between standard, scientific,
    and history management features.
    """

    standard_calc = Calculator()
    history_tools = History()
    scientific_calc = ScientificCalculation()

    while True:

        choice = show_menu()
        if choice == "1":
            handle_standard_calculator(standard_calc, history_tools)
        elif choice == "2":
            handle_scientific_calculator(scientific_calc, history_tools)
        elif choice == "3":
            history_tools.view_history()
        elif choice == "4":
            history_tools.clear_history()
        elif choice == "5":
            view_help()
        elif choice == "6":
            handle_exit()
            break


if __name__ == "__main__":
    main()
