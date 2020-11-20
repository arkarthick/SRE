import pyqrcode
from PIL import Image
import os

BASE_DIR = os.getcwd()


def qr_gen(data, file_name=None, image_name='assets\\logo.jpg'):
	# Generate the qr code and save as png
	if file_name == None:
		file_name = 'temp'
	qrobj = pyqrcode.create(data)
	with open(f'{file_name}.png', 'wb') as f:
	    qrobj.png(f, scale=8)
	img = Image.open(f'{file_name}.png')
	img = img.convert('RGBA')
	if image_name != None:
		# Now open that png image to put the logo
		
		width, height = img.size

		# How big the logo we want to put in the qr code png
		logo_size = 150

		# Open the logo image
		logo = Image.open(image_name)

		# Calculate xmin, ymin, xmax, ymax to put the logo
		xmin = ymin = int((width / 2) - (logo_size / 2))
		xmax = ymax = int((width / 2) + (logo_size / 2))

		# resize the logo as calculated
		logo = logo.resize((xmax - xmin, ymax - ymin))

		# put the logo in the qr code
		img.paste(logo, (xmin, ymin, xmax, ymax))

	# with open(f'{file_name}.png', 'wb') as f:
	#     img.png(f, scale=10)
	img.save(file_name+'.png')

	# img.show()



if __name__ =='__main__':
	data = 'upi://pay?pa=8015031422@upi&pn=Mr RAMKARTHICK  A&am=3300&cu=INR&mode=02&purpose=00&tn=ygu..&orgid=189999&sign=MEYCIQDpxyg4CEMWKXoPjnWZENthh+yQojdxIynSvypTaLHKCAIhALCrEbAk9WwVl68joptBwh+Hnm3JcDbp7MsrObwdfR2J'
	# image = 'sre.jpg'
	qr_gen(data, '3300')