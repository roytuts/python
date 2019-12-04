from fpdf import FPDF, HTMLMixin

#HTML content as text
pdf = FPDF()
pdf.add_page()

#Read file
text = None
with open('file.txt', 'r') as fh:
	text = fh.read()

pdf.set_font('Times', '', 12)
pdf.multi_cell(0, 5, text)

pdf.output('FileContentText2Pdf.pdf', 'F')


#HTML content as HTML
class MyFPDF(FPDF, HTMLMixin):
	pass

pdf = MyFPDF()
pdf.add_page()

html = None
#with open("file.html", "r", encoding='utf-8') as f:
with open("file.txt", "r", encoding='utf-8') as f:
    html= f.read()
	
pdf.write_html(html)
pdf.output('FileContentHtml2Pdf.pdf', 'F')