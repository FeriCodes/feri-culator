class History:
    def __init__(self, filename="CalHistory.txt"):
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
                print(f"- {item}")


    def save_calculation_to_history(self, full_record):
        try:
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(full_record + "\n")
        except IOError:
            print("Error: Could not write to history file.")


    def get_history(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            return []  # if don't have a file return an empty list.
        
    def clear_history_file(self):
        try:
            open(self.filename, "w", encoding="utf-8").close()
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