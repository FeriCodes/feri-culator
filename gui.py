import tkinter as tk
from tkinter import messagebox
from FeriCulator.scientific_calculator import ScientificCalculation
from FeriCulator.history_manager import History


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Feri Culator")
        self.root.geometry("350x490")
        self.root.resizable(False, False)

        self.sci = ScientificCalculation()
        self.history_manager = History()
        self.is_scientific = False

        self.history_btn = tk.Button(
            self.root,
            text="🕒",
            font=("Arial", 14),
            bg="#111111",
            fg="white",
            relief="flat",
            activebackground="#222222",
            activeforeground="white",
            command=self.show_history_window,
        )
        self.history_btn.grid(row=0, column=3, sticky="ne", padx=10, pady=5)

        self.display_label = tk.Label(
            self.root,
            text="0",
            font=("Arial", 24),
            anchor="e",
            bg="#111111",
            fg="white",
        )
        self.display_label.grid(
            row=1, column=0, columnspan=4, sticky="ew", padx=10, pady=10
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
            if int(widget.grid_info()["row"]) > 1:
                widget.destroy()

        if self.is_scientific:
            self.root.geometry("350x490")
            self.is_scientific = False
            self.create_buttons(self.standard_buttons)
        else:
            self.root.geometry("350x590")
            self.is_scientific = True
            self.create_buttons(self.scientific_buttons)

    def create_buttons(self, buttons=None):
        if buttons is None:
            buttons = self.standard_buttons

        row_value = 2
        col_value = 0

        for b_text in buttons:
            btn = tk.Button(
                self.root,
                text=b_text,
                font=("Arial", 14),
                width=5,
                height=2,
                bg="#000000",
                fg="white",
                relief="flat",
                command=lambda x=b_text: self.on_button_click(x),
            )
            btn.grid(row=row_value, column=col_value, padx=5, pady=5)
            col_value += 1

            if col_value == 4:
                col_value = 0
                row_value += 1

    def show_history_window(self):
        hs_window = tk.Toplevel(self.root)
        hs_window.title("Calculation History")
        hs_window.geometry("320x400")
        hs_window.configure(bg="#1a1a1a")
        hs_window.resizable(False, False)

        tk.Label(
            hs_window,
            text="History",
            font=("Arial", 16, "bold"),
            bg="#1a1a1a",
            fg="white",
        ).pack(pady=10)

        hs_text = tk.Text(
            hs_window,
            width=30,
            height=11,
            bg="#111111",
            fg="#cccccc",
            font=("Arial", 14),
            relief="flat",
            state="disabled",
        )
        hs_text.pack(padx=15, pady=5)

        records = self.history_manager.get_history()
        hs_text.config(state="normal")
        if not records:
            hs_text.insert("1.0", "\n  No history found.")
        else:
            for item in records:
                line = f" {item['expression']} = {item['result']}\n ───────\n"
                hs_text.insert("end", line)
        hs_text.config(state="disabled")

        def clear_action():
            if messagebox.askyesno(
                "Clear History", "Do you want to clear history?", parent=hs_window
            ):
                self.history_manager.clear_history()
                hs_text.config(state="normal")
                hs_text.delete("1.0", "end")
                hs_text.insert("1.0", "\n  No history found.")
                hs_text.config(state="disabled")

        clear_btn = tk.Button(
            hs_window,
            text="Clear History",
            font=("Arial", 11, "bold"),
            bg="#d9534f",
            fg="white",
            relief="flat",
            command=clear_action,
        )
        clear_btn.pack(pady=10, fill="x", padx=15)

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

            if not self.expression:
                return

            try:
                num = float(self.expression)
                op_name = "sqrt" if char == "√" else char

                result = self.sci.calculate(op_name, self.expression)

                self.history_manager.save_calculation_to_history(
                    f"{char}({num})", result
                )
                self.expression = str(result) if result != "Math Error" else ""
                self.display_label.config(text=str(result))

            except ValueError:
                self.display_label.config(text="Error")
                self.expression = ""

        # Case 4: Evaluate the mathematical expression
        elif char == "=":
            if not self.expression:
                return
            try:
                result = eval(self.expression)
                self.history_manager.save_calculation_to_history(
                    self.expression, result
                )

                self.expression = str(result)
                self.display_label.config(text=self.expression)

            except Exception:
                self.display_label.config(text="Error")
                self.expression = ""

        # Case 5: Switch between standard and scientific modes
        elif char in ["SCI", "STD"]:
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
