"""
FeriCulator: A scientific calculator with history management.
Main entry point of the application launching the GUI interface.
"""

import customtkinter as ctk
from src.gui import CalculatorApp


def main():
    """
    Initializes the main Tkinter window and starts the CalculatorApp.
    """
    root = ctk.CTk()
    _ = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
