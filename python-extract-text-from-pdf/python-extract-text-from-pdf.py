#Importing PDF reader PyPDF2
import PyPDF2

#Open file Path
pdf_File = open('simple.pdf', 'rb') 

#Create PDF Reader Object
pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
count = pdf_Reader.numPages # counts number of pages in pdf
TextList = []

#Extracting text data from each page of the pdf file
for i in range(count):
   try:
    page = pdf_Reader.getPage(i)
    TextList.append(page.extractText())
   except:
       pass

#Converting multiline text to single line text
TextString = " ".join(TextList)

print(TextString)