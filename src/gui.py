import customtkinter as ctk
from tkinter import messagebox
from src.handlers import Handlers
from src.scientific_calculator import ScientificCalculation
from src.history_manager import History


class CalculatorApp:
    """
    The main GUI class for the FeriCulator application.
     - Initializes the main window and its widgets.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Feri Culator")
        self.root.geometry("350x490")
        self.root.resizable(False, False)
        self.root.configure(fg_color="#171717")

        # Initialize the scientific calculator and history manager
        self.sci = ScientificCalculation()
        self.history_manager = History()

        # the key for accessing the handlers of the buttons and other widgets in the GUI.
        self.handlers = Handlers(self)

        self.history_btn = ctk.CTkButton(
            self.root,
            text="🕒",
            font=("Arial", 16, "bold"),
            command=self.show_history_window,
            fg_color="#171717",
            hover_color="#2a2a2a",
            text_color="#ff9f0a",
            width=40,
            height=40,
        )
        self.history_btn.grid(row=0, column=3, sticky="ne", padx=10, pady=5)

        self.display_label = ctk.CTkLabel(
            self.root,
            text="0",
            font=("Arial", 32),
            anchor="e",
            fg_color="#171717",
            text_color="white",
            width=320,
            height=60,
        )
        self.display_label.grid(
            row=1, column=0, columnspan=4, sticky="ew", padx=10, pady=10
        )

        # fmt: off
        self.standard_buttons = [
            "AC", "C", "%", "÷",
            "7", "8", "9", "×",
            "4", "5", "6", "−",
            "1", "2", "3", "+",
            "SCI", "0", ".", "="
        ]
        
        self.scientific_buttons = [
            "sin", "cos", "tan", "cot",
            "fac", "π", "√", "log",
            "AC", "C", "%", "÷",
            "7", "8", "9", "×",
            "4", "5", "6", "−",
            "1", "2", "3", "+",
            "STD","0", ".", "="
        ]
        # fmt: on

        self.create_buttons()

    def update_gui_mode(self, is_scientific):
        """
        Handles all UI changes for switching between Standard and Scientific modes.
        """

        for widget in self.root.grid_slaves():
            if int(widget.grid_info()["row"]) > 1:
                widget.destroy()

        if is_scientific:
            self.root.geometry("350x630")
            self.create_buttons(self.scientific_buttons)
        else:
            self.root.geometry("350x490")
            self.create_buttons(self.standard_buttons)

    def create_buttons(self, buttons=None):
        if buttons is None:
            buttons = self.standard_buttons

        row_value = 2
        col_value = 0

        for b_text in buttons:

            button_bg = "#222222"
            button_fg = "#FFFFFF"
            hover_color = "#333333"

            if b_text in ["AC", "C", "%"]:
                button_bg = "#171717"
                button_fg = "#ff9f0a"
                hover_color = "#2a2a2a"

            elif b_text in ["÷", "×", "−", "+", "SCI", "STD"]:
                button_bg = "#171717"
                button_fg = "#ff9f0a"
                hover_color = "#2a2a2a"

            elif b_text == "=":
                button_bg = "#ff9f0a"
                button_fg = "#FFFFFF"
                hover_color = "#cc7f00"

            elif b_text in ["sin", "cos", "tan", "cot", "fac", "π", "√", "log"]:
                button_bg = "#171717"
                button_fg = "#64ffda"
                hover_color = "#2a2a2a"

            btn = ctk.CTkButton(
                self.root,
                text=b_text,
                font=("Arial", 21, "bold"),
                fg_color=button_bg,
                text_color=button_fg,
                hover_color=hover_color,
                width=75,
                height=60,
                corner_radius=10,
                command=lambda x=b_text: self.handlers.on_button_click(x),
            )
            btn.grid(row=row_value, column=col_value, padx=5, pady=5)
            col_value += 1

            if col_value == 4:
                col_value = 0
                row_value += 1

    def show_history_window(self):
        hs_window = ctk.CTkToplevel(self.root)
        hs_window.title("Calculation History")
        hs_window.geometry("320x400")
        hs_window.configure(fg_color="#171717")

        hs_window.resizable(False, False)

        hs_window.attributes("-topmost", True)
        hs_window.transient(self.root)
        hs_window.lift()
        hs_window.focus_force()

        ctk.CTkLabel(
            hs_window, text="History", font=("Arial", 16, "bold"), text_color="#FFFFFF"
        ).pack(pady=10)

        hs_text = ctk.CTkTextbox(
            hs_window,
            width=280,
            height=250,
            font=("Arial", 18),
            fg_color="#000000",
            text_color="#FFFFFF",
        )
        hs_text.pack(padx=15, pady=5)

        records = self.history_manager.get_history()
        hs_text.configure(state="normal")
        if not records:
            hs_text.insert("1.0", "\n  No history found.")
        else:
            for item in records:
                line = f" {item['expression']} = {item['result']}\n ───-----\n"
                hs_text.insert("end", line)
        hs_text.configure(state="disabled")

        def clear_action():
            if messagebox.askyesno(
                "Clear History",
                "Do you want to clear history?",
                parent=hs_window,
            ):
                self.history_manager.clear_history()
                hs_text.configure(state="normal")
                hs_text.delete("1.0", "end")
                hs_text.insert("1.0", "\n  No history found.")
                hs_text.configure(state="disabled")

        clear_btn = ctk.CTkButton(
            hs_window,
            text="Clear History",
            font=("Arial", 14, "bold"),
            command=clear_action,
            fg_color="#ff9f0a",
            hover_color="#cc7f00",
            width=30,
            height=30,
        )
        clear_btn.pack(pady=10, fill="x", padx=15)
