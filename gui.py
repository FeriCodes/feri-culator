import tkinter as tk


class Ferigui:
    def __init__(self, root):
        self.root = root
        self.root.title("Feri Culator")
        self.root.geometry("350x450")

        self.display_label = tk.Label(
            self.root, text="0", font=("Arial", 20), anchor="e"
        )
        self.display_label.grid(row=0, column=0, columnspan=4, pady=20)


if __name__ == "__main__":
    window = tk.Tk()
    app = Ferigui(window)
    window.mainloop()
