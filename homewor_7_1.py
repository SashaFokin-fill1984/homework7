from zipfile import ZipFile
from pypdf import PdfReader
from openpyxl import load_workbook
from io import BytesIO

def test_arc_pdf(create_archive_file):
    with ZipFile("homework_7.zip", "r") as archive:
        print(archive.namelist())
        with archive.open('1718880779_Verzani-SimpleR.pdf') as pdf_file:
            reader = PdfReader(pdf_file)
            # first_page_text = reader.pages[0].extract_text()


