import tkinter as tk


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Feri Culator")
        self.root.geometry("350x450")
        self.display_label = tk.Label(
            self.root,
            text="0",
            font=("Arial", 24),
            anchor="e",
            bg="#111111",
            fg="white",
        )
        self.display_label.grid(row=0, column=0, columnspan=4, sticky="ew", pady=20)
        self.root.configure(bg="#111111")

        # fmt: off
        self.buttons = [
            "AC", "C", "%", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "()", "0", ".", "="
        ]
        # fmt: on

        # self.expression stores the current mathematical formula as a string
        self.expression = ""

        self.create_buttons()

    def create_buttons(self):
        row_value = 1
        col_value = 0

        for b_text in self.buttons:
            self.btn = tk.Button(
                self.root,
                text=b_text,
                font=("Arial", 14),
                padx=20,
                pady=20,
                bg="#222222",
                fg="white",
                relief="flat",
                command=lambda x=b_text: self.on_button_click(x),
            )
            self.btn.grid(row=row_value, column=col_value)
            col_value += 1

            if col_value == 4:
                col_value = 0
                row_value += 1

    def on_button_click(self, char):
        # Case 1: Clear everything if AC is pressed
        if char == "AC":
            self.expression = ""
            self.display_label.configure(text="0")

        # Case 2: Delete the last character if C is pressed (Backspace)
        elif char == "C":
            self.expression = self.expression[:-1]
            if self.expression == "":
                self.display_label.config(text="0")
            else:
                self.display_label.config(text=self.expression)

        # Case 3: Append the number or operator to the expression
        else:
            self.expression += char
            self.display_label.config(text=self.expression)

        print(f"You clicked: {char}")


if __name__ == "__main__":
    window = tk.Tk()
    app = CalculatorApp(window)
    window.mainloop()
