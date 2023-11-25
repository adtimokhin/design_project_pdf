# gui/main_window.py
import tkinter as tk

class MainWindow:
    def __init__(self, root, button_function):
        self.root = root
        self.root.title("PDF Generator")
        self.root.geometry("800x600")
        self.root.configure(bg="white")

        # Add a text field
        self.text_field = tk.Text(self.root, height=10, width=50)
        self.text_field.pack(pady=30)

        # Add a button to toggle fullscreen
        self.fullscreen_button = tk.Button(self.root, text="Generate PDF", command=button_function)
        self.fullscreen_button.pack(pady=10)
        