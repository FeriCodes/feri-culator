class Handlers:
    """
    handeling the events of the buttons and other widgets in the GUI.

    """

    def __init__(self, app):
        # 'app' is the key to access the GUI widgets (like display_label)
        self.app = app
        self.is_scientific = False
        self.expression = ""

    def toggle_mode(self):
        for widget in self.app.root.grid_slaves():
            if int(widget.grid_info()["row"]) > 1:
                widget.destroy()

        if self.is_scientific:
            self.app.root.geometry("350x490")
            self.is_scientific = False
            self.app.create_buttons(self.app.standard_buttons)
        else:
            self.app.root.geometry("350x630")
            self.is_scientific = True
            self.app.create_buttons(self.app.scientific_buttons)

    def on_button_click(self, char):
        if char == "AC":
            self.expression = ""
            self.app.display_label.configure(text="0")

        elif char == "C":
            self.expression = self.expression[:-1]
            if self.expression == "":
                self.app.display_label.configure(text="0")
            else:
                self.app.display_label.configure(text=self.expression)

        elif char in ["sin", "cos", "tan", "cot", "fac", "π", "log", "√"]:
            if char == "π":
                result = self.app.sci.calculate_pi()
                self.expression = str(result)
                self.app.display_label.configure(text=self.expression)
                return

            if not self.expression:
                return

            try:
                num = float(self.expression)
                op_name = "sqrt" if char == "√" else char
                result = self.app.sci.calculate(op_name, self.expression)

                if result != "Math Error":
                    self.app.history_manager.save_calculation_to_history(
                        f"{char}({num})", result
                    )
                    self.expression = str(result)
                else:
                    self.expression = ""

                self.app.display_label.configure(text=str(result))

            except ValueError:
                self.app.display_label.configure(text="Error")
                self.expression = ""

        elif char == "=":
            if not self.expression:
                return
            try:
                clean_expression = (
                    self.expression.replace("÷", "/")
                    .replace("×", "*")
                    .replace("−", "-")
                )

                result = eval(clean_expression)

                self.app.history_manager.save_calculation_to_history(
                    self.expression, result
                )

                self.expression = str(result)
                self.app.display_label.configure(text=self.expression)

            except Exception:
                self.app.display_label.configure(text="Error")
                self.expression = ""

        elif char in ["SCI", "STD"]:
            self.toggle_mode()

        else:
            self.expression += char
            self.app.display_label.configure(text=self.expression)
