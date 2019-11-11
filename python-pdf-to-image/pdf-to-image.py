from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

#images = convert_from_path('sample.pdf')
#for image in images:
    #image.save('sample.png', 'PNG')
	
#images = convert_from_path('gentleman.pdf')
#for image in images:
    #image.save('gentleman.jpg', 'JPEG')
	
#images = convert_from_bytes(open('gentleman.pdf', 'rb').read())
#images[0].save('gentleman-byte.jpg', 'JPEG')

#images = convert_from_path('output1.pdf')
#i = 1
#for image in images:
	#image.save('output' + str(i) + '.jpg', 'JPEG')
	#i = i + 1