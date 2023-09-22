import PyPDF2

page_number_1 = int(input("Enter a page number from the first PDF to merge:"))
page_number_2 = int(input("Enter a page number from the second PDF to merge:"))
page_number_3 = int(input("Enter a page number from the third PDF to merge:"))

pdf_writer = PyPDF2.PdfWriter()

pdf_file_1 = open('file_1.pdf', 'rb')
pdf_reader_1 = PyPDF2.PdfReader(pdf_file_1)
pdf_writer.add_page(pdf_reader_1.pages[page_number_1 - 1])

pdf_file_2 = open('file_2.pdf', 'rb')
pdf_reader_2 = PyPDF2.PdfReader(pdf_file_2)
pdf_writer.add_page(pdf_reader_2.pages[page_number_2 - 1])

pdf_file_3 = open('file_3.pdf', 'rb')
pdf_reader_3 = PyPDF2.PdfReader(pdf_file_3)
pdf_writer.add_page(pdf_reader_3.pages[page_number_3 - 1])

output_pdf_file = 'output.pdf'

with open(output_pdf_file, 'wb') as output_pdf:
    pdf_writer.write(output_pdf)

pdf_file_1.close()
pdf_file_2.close()
pdf_file_3.close()

print('New PDF created successfully')
