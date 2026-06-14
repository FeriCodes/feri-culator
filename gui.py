import tkinter as tk
from FeriCulator.scientific_calculator import ScientificCalculation


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Feri Culator")
        self.root.geometry("350x450")
        self.root.resizable(False, False)

        self.sci = ScientificCalculation()
        self.is_scientific = False

        self.display_label = tk.Label(
            self.root,
            text="0",
            font=("Arial", 24),
            anchor="e",
            bg="#111111",
            fg="white",
        )
        self.display_label.grid(
            row=0, column=0, columnspan=4, sticky="ew", padx=10, pady=20
        )
        self.root.configure(bg="#111111")

        # fmt: off
        self.standard_buttons = [
            "AC", "C", "%", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "SCI", "0", ".", "="
        ]
        
        self.scientific_buttons = [
            "sin", "cos", "tan", "cot",
            "fac", "π", "√", "log",
            "AC", "C", "%", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "STD","0", ".", "="
        ]
        # fmt: on

        # self.expression stores the current mathematical formula as a string
        self.expression = ""

        self.create_buttons()

    def toggle_mode(self):
        for widget in self.root.grid_slaves():
            if int(widget.grid_info()["row"]) > 0:
                widget.destroy()

        if self.is_scientific:
            self.root.geometry("350x470")
            self.is_scientific = False
            self.create_buttons(self.standard_buttons)
        else:
            self.root.geometry("350x570")
            self.is_scientific = True
            self.create_buttons(self.scientific_buttons)

    def create_buttons(self, buttons=None):
        if buttons is None:
            buttons = self.standard_buttons

        row_value = 1
        col_value = 0

        for b_text in buttons:
            btn = tk.Button(
                self.root,
                text=b_text,
                font=("Arial", 14),
                width=5,
                height=2,
                bg="#222222",
                fg="white",
                relief="flat",
                command=lambda x=b_text: self.on_button_click(x),
            )
            btn.grid(row=row_value, column=col_value, padx=5, pady=5)
            col_value += 1

            if col_value == 4:
                col_value = 0
                row_value += 1

    def on_button_click(self, char):
        # Case 1: Clear the entire expression and reset display
        if char == "AC":
            self.expression = ""
            self.display_label.configure(text="0")

        # Case 2: Delete the last entered character (Backspace)
        elif char == "C":
            self.expression = self.expression[:-1]

            if self.expression == "":
                self.display_label.config(text="0")
            else:
                self.display_label.config(text=self.expression)

        # Case 3: Handle scientific calculator operations
        elif char in ["sin", "cos", "tan", "cot", "fac", "π", "log", "√"]:

            if char == "π":
                result = self.sci.calculate_pi()
                self.expression = str(result)
                self.display_label.config(text=self.expression)
                return

            # Ignore scientific operations if no input exists
            if not self.expression and char != "π":
                return

            try:
                num = float(self.expression)

                if char == "sin":
                    result = self.sci.calculate_sin(num)

                elif char == "cos":
                    result = self.sci.calculate_cos(num)

                elif char == "tan":
                    result = self.sci.calculate_tan(num)

                elif char == "cot":
                    result = self.sci.calculate_cot(num)

                elif char == "fac":
                    result = self.sci.calculate_factorial(int(num))

                elif char == "log":
                    result = self.sci.calculate_log(num)

                elif char == "√":
                    result = self.sci.calculate_sqrt(num)

                # Update calculator state and display result
                self.expression = str(result)
                self.display_label.config(text=self.expression)

            except ValueError:
                self.display_label.config(text="Error")
                self.expression = ""

        # Case 4: Evaluate the mathematical expression
        elif char == "=":
            try:
                result = eval(self.expression)
                self.expression = str(result)
                self.display_label.config(text=self.expression)

            except Exception:
                self.display_label.config(text="Error")
                self.expression = ""

        # Case 5: Switch between standard and scientific modes
        elif char == "SCI":
            self.toggle_mode()

        elif char == "STD":
            self.toggle_mode()

        # Case 6: Append numbers and operators to the expression
        else:
            self.expression += char
            self.display_label.config(text=self.expression)

        print(f"You clicked: {char}")


if __name__ == "__main__":
    window = tk.Tk()
    app = CalculatorApp(window)
    window.mainloop()
