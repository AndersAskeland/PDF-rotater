# %%
from PyPDF2 import PdfFileReader
from pathlib import Path
from pdf2image import convert_from_path

# Create class
class Pdf_document:
    # Page stuff. Is defined later on
    page_nr = 0

    def __init__(self, location):
        # Reader stuff
        self.pdf_read = self.pdf_reader(location)
        self.title = self.pdf_read.documentInfo.title
        self.pages = self.pdf_read.getNumPages

        # Writer stuff
        self.pdf_write = self.pdf_writer(location)

        # Current page
        self.current_page = Pdf_page(pdf_document=self.pdf_read, page=self.page_nr)

    def pdf_reader(self, location):
        return PdfFileReader(str(location))

    def pdf_writer(self, location):
        pass
    
    def rotate(self, direction):
        pass

class Pdf_page:
    def __init__(self, pdf_document, page):
        self.page = pdf_document.getPage(page)
        self.text = self.page.extractText()


# Set path
pdf_path = Path("PDFs/researchfish_common_outcomes_overview_january2020.pdf")

# PDF file
pdf = PdfFileReader(str(pdf_path))

# Get number of pages
pdf.getNumPages()

# Get title
pdf.documentInfo.title

# Test using classes
selected_pdf = Pdf_document(Path("PDFs/researchfish_common_outcomes_overview_january2020.pdf"))

print(selected_pdf.title)

print(f"Current page text is:\n {selected_pdf.current_page.text}") # Class within a class


# Convert to JPG
pages = convert_from_path(pdf_path, 500)


    
# %%
