from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 


font_50 = ImageFont.truetype("fonts\\calibri.ttf", 50)
font_70 = ImageFont.truetype("fonts\\calibri.ttf", 70)
font_80 = ImageFont.truetype("fonts\\calibri.ttf", 80)
font_90 = ImageFont.truetype("fonts\\calibri.ttf", 90)


def invoice_write(details, qr=None):
	bill_img = 'assets\\invoice_template.jpg'
	img=Image.open(bill_img)
	draw = ImageDraw.Draw(img)

	draw.text((250, 760), details['name'],(0,0,0),font=font_70)
	draw.text((250, 845), details['phone_no'],(0,0,0),font=font_70)
	draw.text((250, 925), details['mobile'],(0,0,0),font=font_70)
	draw.text((1980, 550), details['account_no'],(0,0,0),font=font_70)
	draw.text((530, 550), details['invoice_no'],(0,0,0),font=font_70)

	draw.text((635, 1210), details['bill_date'],(0,0,0),font=font_70)
	draw.text((170, 1500), '1',(0,0,0),font=font_70)
	draw.text((255, 1500), 'Bandwidth charge for last month',(0,0,0),font=font_70)
	draw.text((255, 1570), '(GST Included)',(0,0,0),font=font_50)
	draw.text((1850, 1500), details['bill_amt'],(0,0,0),font=font_70)
	draw.text((2090, 650), details['ex_code'],(0,0,0),font=font_70)
	# draw.text((1600, 2400), '18% of Rs.',(0,0,0),font=font_80)
	if qr != None:
		qr_img = Image.open(qr)
		img.paste(qr_img, (1600, 2225))

	# draw.text((2000, 1700), details['plan_amount'],(0,0,0),font=font_80)
	# draw.text((2000, 2200), details['tax_amount'],(0,0,0),font=font_80)
	draw.text((1850, 2100), details['bill_amt'],(0,0,0),font=font_90)
	
	img.save('Bills\\'+details['bill_date']+'\\'+details['phone_no']+'.png')


def ont_bill_write(details, qr=None):
	bill_img = 'assets\\ont_bill_template.jpg'
	img=Image.open(bill_img)
	draw = ImageDraw.Draw(img)

	draw.text((250, 760), details['name'],(0,0,0),font=font_70)
	draw.text((250, 845), '04633-'+str(details['phone_no']),(0,0,0),font=font_70)
	draw.text((250, 930), str(details['mobile']),(0,0,0),font=font_70)
	draw.text((250, 1015), details['area'],(0,0,0),font=font_70)
	draw.text((450, 560), str(details['bill_no']),(0,0,0),font=font_70)
	draw.text((1770, 560), details['date'],(0,0,0),font=font_70)
	draw.text((170, 1500), '1',(0,0,0),font=font_70)
	draw.text((255, 1500), details['description'],(0,0,0),font=font_70)
	draw.text((255, 1570), '(18% GST Included)',(0,0,0),font=font_50)
	draw.text((1850, 1500), str(details['bill_amt']),(0,0,0),font=font_70)
	draw.text((2090, 650), details['ex_code'],(0,0,0),font=font_70)
	# draw.text((1600, 2400), '18% of Rs.',(0,0,0),font=font_80)
	try:
		if qr != None:
			qr_img = Image.open(qr)
			img.paste(qr_img, (1600, 2215))
	except:
		print('image writer qr write failed')

	# draw.text((2000, 1700), details['plan_amount'],(0,0,0),font=font_80)
	# draw.text((2000, 2200), details['tax_amount'],(0,0,0),font=font_80)
	draw.text((1850, 2100), str(details['bill_amt']),(0,0,0),font=font_90)
	
	img.save('Bills\\ONT\\'+details['phone_no']+'.png')


if __name__ == '__main__':
	pass