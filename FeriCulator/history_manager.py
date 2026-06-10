"""
History module for FeriCulator.
Manages saving, viewing, and clearing calculation history in a JSON file.
"""

import json
import os
from datetime import datetime


class History:
    """
    Handles calculation history management, including saving, viewing, and clearing history records.
    """

    def __init__(self, filename="CalHistory.json"):
        self.filename = filename

    def view_history(self):
        """
        2- choice 2 in main menu for display calculation history.
        """
        print("\n--- Calculation History ---")
        history = self.get_history()
        if not history:
            print("No history found.")
        else:
            for item in history:
                print(f"[{item['time']}] {item['expression']} = {item['result']}")

    def save_calculation_to_history(self, expression, result):
        """
        Saves a calculation record to the history JSON file.
        Each record includes the expression, result, and timestamp.له
        """

        history = self.get_history()
        new_record = {
            "expression": expression,
            "result": result,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        history.append(new_record)

        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(history, file, indent=4, ensure_ascii=False)
        except IOError:
            print("Error: Could not write to history file.")

    def get_history(self):
        """
        Retrieves the calculation history from the JSON file.
        """
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []  # if don't have a file return an empty list.

    def clear_history_file(self):
        """
        Clears the history file by overwriting it with an empty list.
        """
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump([], file)
        except IOError:
            print("Error: Could not clear history file.")

    def clear_history(self):
        """
        choice 3 in main manu for getting clear history.
        """

        print("do you want to clear calculation history? (y/n): ")

        confirm = input().strip().lower()
        if confirm != "y":
            print("Operation cancelled. History not cleared.")
            return

        print("\nClearing calculation history...")
        self.clear_history_file()
        print("History cleared!")
