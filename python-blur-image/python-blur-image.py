from PIL import Image, ImageFilter
import os

img_dir = "C:/python/python-blur-image/"
img_name = 'original.jpg'
img = Image.open(img_dir + img_name)
f, e = os.path.splitext(img_dir + img_name)

blur_img = img.filter(ImageFilter.BLUR)
blur_img.save(f + '_blurred.jpg')

box_blur_img = img.filter(ImageFilter.BoxBlur(7))
box_blur_img.save(f + '_box_blurred.jpg')

gaus_blur_img = img.filter(ImageFilter.GaussianBlur(7))
gaus_blur_img.save(f + '_gaus_blurred.jpg')