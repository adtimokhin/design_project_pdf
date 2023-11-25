# main.py
import tkinter as tk
from gui import MainWindow  # Assuming your package is named "gui"
from pdf_generator import PDFGenerator



# Create the main window
root = tk.Tk()

# Function that will take the tex from the text field and generate a PDF with those contents
def generate_pdf():
    print("Generating PDF...")
    output_file_path = "pdfs/hello_world.pdf"
    pdf_generator = PDFGenerator(output_file_path)
    pdf_generator.generate_hello_world_pdf()
    print(f"PDF generated at: {output_file_path}")


# Instantiate MainWindow
main_window = MainWindow(root, generate_pdf)

# Run the Tkinter event loop
root.mainloop()


