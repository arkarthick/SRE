import os
from time import strftime, sleep
import json
from datetime import datetime
from qr_gen import qr_gen
from image_writer import ont_bill_write


BASE_DIR = os.getcwd()
snc_obj = open('data\\TVLSNC.json')
vki_obj = open('data\\TVLVKI.json')
SNC = json.loads(snc_obj.read())
VKI = json.loads(vki_obj.read())

dic = {**SNC, **VKI}

def ont_bill_gen(tel_num=None, date=None, name=None, description=None, ammount=None):
	data = {}
	
	if name != None:
		data['name'] = name
	else:
		data['name'] = dic[tel_num]['NAME']
	data['bill_no'] = dic[tel_num]['Bill No']
	data['phone_no'] = tel_num
	data['mobile'] = dic[tel_num]['MOBILE']
	data['ex_code'] = dic[tel_num]['EXG CODE']
	if description != None:
		data['description'] = description
	else:
		data['description'] = 'Optical Modem and Installation charges'
	if date != None:
		data['date'] = date
	else:
		data['date'] = dic[tel_num]['Date']
	if ammount != None:
		data['bill_amt'] = ammount
	else:
		data['bill_amt'] = dic[tel_num]['ONT Amount']
                # if dic[tel_num]['ONT Amount'] != '' and dic[tel_num]['ONT Amount'] != None:
                #         data['bill_amt'] = dic[tel_num]['ONT Amount']
                # else:
                #         print('ammount not specified')
	if data['ex_code'] == 'TVLSNC':
		data['area'] = 'Shengottah'
	elif data['ex_code'] == 'TVLVKI':
		data['area'] = 'Vadakarai'



	# return(data)

	# if tel_num != None and tel_num != '':
	bill_amt = data['bill_amt']
	remarks = data['phone_no'],data['ex_code'],data['name'], ' for ont'
	# ex_code = 
	url = f'upi://pay?pa=8015031422@upi&pn=Mr RAMKARTHICK  A&am={bill_amt}&cu=INR&mode=02&purpose=00&tn={remarks}&orgid=189999&sign=MEYCIQDpxyg4CEMWKXoPjnWZENthh+yQojdxIynSvypTaLHKCAIhALCrEbAk9WwVl68joptBwh+Hnm3JcDbp7MsrObwdfR2J'

	try:
		qr = qr_gen(url)
	except:
		print(' qrgen failed')

	try:
		ont_bill_write(data, 'temp.png')
		print(data['phone_no'])
	except:
		print('img write faled')

	# ont_bill_write(data, 'temp.png')
	
	
def custom_bill():
	tel = input('Enter telephone number > ')
	ammount = input('Ammount > ')
	if ammount == '':
		ammount = None
	date = input('date > ')
	if date == '':
		date = None
	ont_bill_gen(tel_num=tel, date=date, ammount=ammount)

def gen_bill_for_all():
	for _ in dic:
		if _ != '':
			ont_bill_gen(_)

def main():
	gen_type = input('''press,
	1 to make customm bill
	2 to generate bill for all ''')
	if gen_type == '1':
		custom_bill()
	elif gen_type == '2':
		gen_bill_for_all()

if __name__ == '__main__':
	main()

        
