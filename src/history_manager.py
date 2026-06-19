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

    def __init__(self, filename="CalHistory.json", max_records=50):

        base_dir = os.path.dirname(os.path.abspath(__file__))

        self.filename = os.path.join(base_dir, filename)
        self.max_records = max_records

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

    def save_calculation_to_history(self, expression, result):
        """
        Saves a calculation record to the history JSON file.
        Each record includes the expression, result, and timestamp.
        """
        history = self.get_history()
        new_record = {
            "expression": expression,
            "result": result,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        history.append(new_record)

        if len(history) > self.max_records:
            history = history[-self.max_records :]

        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(history, file, indent=4, ensure_ascii=False)
        except IOError:
            print("Error: Could not write to history file.")

    def clear_history(self):
        """
        Cleals the history file by overwriting it with an empty list.
        """
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump([], file)
        except IOError:
            print("Error: Could not clear history file.")
