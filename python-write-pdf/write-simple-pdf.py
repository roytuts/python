from fpdf import FPDF

pdf = FPDF()

#header of the pdf file
header = 'Header of PDF Report'
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
w = pdf.get_string_width(header) + 6
pdf.set_x((210 - w) / 2)
pdf.cell(w, 9, header, 0, 0, 'C')
pdf.line(20, 18, 210-20, 18)

#line break
pdf.ln(10)
pdf.set_font('Times', '', 12)
pdf.multi_cell(0, 5, 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.')

pdf.ln()
pdf.set_font('Arial', '', 12)
pdf.set_fill_color(200, 220, 255)
pdf.cell(0, 6, 'Chapter %d : %s' % (1, 'Sample Label'), 0, 1, 'L', 1)

pdf.ln()
pdf.set_font('Courier', 'B', 12)
pdf.multi_cell(0, 5, 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.')

pdf.ln()
pdf.set_font('', 'U', 11)
pdf.multi_cell(0, 6, 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using \'Content here, content here\', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for \'lorem ipsum\' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose.')

pdf.ln()
pdf.set_font('', 'I')
pdf.cell(0, 5, 'This is italic text')

#pdf.set_y(0)
pdf.set_y(-30)
pdf.set_font('Arial', '', 8)
pdf.set_text_color(0)
pdf.cell(0, 5, 'Page ' + str(pdf.page_no()), 0, 0, 'C')

pdf.output('simple.pdf', 'F')