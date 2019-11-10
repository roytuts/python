import img2pdf

#opening from filename
with open("gentleman.pdf","wb") as f:
	f.write(img2pdf.convert('gentleman.png'))
	
with open("sample.pdf","wb") as f:
	f.write(img2pdf.convert('sample.jpg'))
	
#multiple inputs (variant 1)
with open("output1.pdf","wb") as f:
	f.write(img2pdf.convert("gentleman.png", "sample.jpg"))
	
#multiple inputs (variant 2)
with open("output2.pdf","wb") as f:
	f.write(img2pdf.convert(["gentleman.png", "sample.jpg"]))

#specify paper size (A4)
a4inpt = (img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
layout_fun = img2pdf.get_layout_fun(a4inpt)
with open("paper_size.pdf","wb") as f:
	f.write(img2pdf.convert('sample.jpg', layout_fun=layout_fun))