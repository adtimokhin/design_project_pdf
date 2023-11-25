from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class PDFGenerator:
    def __init__(self, output_file):
        self.output_file = output_file

    def generate_hello_world_pdf(self):
        # Create a PDF document
        pdf_canvas = canvas.Canvas(self.output_file, pagesize=letter)

        # Set font and font size
        pdf_canvas.setFont("Helvetica", 14)

        # Set text color (black)
        pdf_canvas.setFillColorRGB(0, 0, 0)

        # Add text to the PDF
        pdf_canvas.drawString(100, 700, "Hello World!")

        # Save the PDF file
        pdf_canvas.save()
