import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Feri-Culator")
        self.root.geometry("350x500")


root = ctk.CTk()
app = CalculatorApp(root)
root.mainloop()
