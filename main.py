"""
FeriCulator: A scientific calculator with history management.
Main entry point of the application launching the GUI interface.
"""

import tkinter as tk
from FeriCulator.gui import CalculatorApp


def main():
    """
    Initializes the main Tkinter window and starts the CalculatorApp.
    """
    root = tk.Tk()
    _ = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
