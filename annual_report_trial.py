import PyPDF2
mypdf = open('Coke2017annualreview.pdf', mode='rb')
pdf_document = PyPDF2.PdfFileReader(mypdf)

for i in range(pdf_document.numPages):
    page_to_print = pdf_document.getPage(i)
    print(page_to_print.extractText())
