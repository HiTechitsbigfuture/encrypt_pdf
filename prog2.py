from PyPDF2 import PdfWriter, PdfReader

writer = PdfWriter()
pdf = PdfReader('Python_all_in_one (2).pdf')

for page in pdf.pages:
    writer.add_page(page)


writer.encrypt('password')

with open('protected.pdf', 'wb') as f:
    writer.write(f)
