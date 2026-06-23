class Handlers:
    """
    handeling the events of the buttons and other widgets in the GUI.

    """

    def __init__(self, app):
        # 'app' is the key to access the GUI widgets (like display_label)
        self.app = app
        self.is_scientific = False
        self.expression = ""

    def format_display(self, value):
        """
        Formats the value to fit inside the display without breaking the GUI.
        """
        val_str = str(value)

        if len(val_str) > 12:
            try:

                return f"{float(value):.5e}"
            except ValueError:
                return val_str[:12]
        return val_str

    def toggle_mode(self):
        """
        Toggles the internal state and requests the GUI to update its layout.
        """
        self.is_scientific = not self.is_scientific

        self.app.update_gui_mode(self.is_scientific)

    def on_button_click(self, char):
        """
        Handles the button click events and updates the display accordingly.
        """
        if char == "AC":
            self.expression = ""
            self.app.display_label.configure(text="0")

        elif char == "C":
            self.expression = self.expression[:-1]
            if self.expression == "":
                self.app.display_label.configure(text="0")
            else:
                formatted_text = self.format_display(self.expression)
                self.app.display_label.configure(text=formatted_text)

        elif char in ["sin", "cos", "tan", "cot", "fac", "π", "log", "√"]:
            if char == "π":
                result = self.app.sci.calculate_pi()
                self.expression = str(result)

                formatted_text = self.format_display(self.expression)
                self.app.display_label.configure(text=formatted_text)
                return

            if not self.expression:
                return

            try:
                num = float(self.expression)
                op_name = "sqrt" if char == "√" else char
                result = self.app.sci.calculate(op_name, self.expression)

                if result != "Math Error":
                    if isinstance(result, float):
                        result = round(result, 10)
                        if result.is_integer():
                            result = int(result)

                    self.app.history_manager.save_calculation_to_history(
                        f"{char}({num})", result
                    )
                    self.expression = str(result)
                else:
                    self.expression = ""

                formatted_text = self.format_display(result)
                self.app.display_label.configure(text=formatted_text)

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

                if isinstance(result, float):
                    result = round(result, 10)
                    if result.is_integer():
                        result = int(result)

                self.app.history_manager.save_calculation_to_history(
                    self.expression, result
                )

                self.expression = str(result)

                formatted_text = self.format_display(self.expression)
                self.app.display_label.configure(text=formatted_text)

            except Exception:
                self.app.display_label.configure(text="Error")
                self.expression = ""

        elif char in ["SCI", "STD"]:
            self.toggle_mode()

        else:
            self.expression += char

            formatted_text = self.format_display(self.expression)
            self.app.display_label.configure(text=formatted_text)
