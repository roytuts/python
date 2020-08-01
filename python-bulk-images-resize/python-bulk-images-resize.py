import PIL
import os
import os.path
from PIL import Image

img_dir = r'C:/MyDocuments/roytuts/feature-images/temp/'

print('Bulk images resizing started...')

for img in os.listdir(img_dir):
	f_img = img_dir + img
	f, e = os.path.splitext(img_dir + img)
	img = Image.open(f_img)
	img = img.resize((1200, 628))
	#img.save(f + '_resized.jpg')
	img.save(f_img)

print('Bulk images resizing finished...')

#from PIL import Image
#import os, sys

#img_dir = "C:/MyDocuments/roytuts/feature-images/resized-2/"
#dirs = os.listdir( img_dir )

#def resize_bulk_images():
#	for img in dirs:
#		if os.path.isfile(img_dir + img):
#			im = Image.open(img_dir + img)
#			f, e = os.path.splitext(img_dir + img)
#			imResize = im.resize((1200, 628), Image.ANTIALIAS)
#			imResize.save(f + '_resized.jpg', 'JPEG', quality=90)

#print('Bulk images resizing started...')
#resize_bulk_images()
#print('Bulk images resizing finished...')