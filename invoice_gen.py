import os
from datetime import datetime
import getpass
import xlrd
from time import strftime, sleep
import xl_to_json
from xl_to_json import opensheet, create_json
import json
from image_writer import invoice_write
from qr_gen import qr_gen
import time


BASE_DIR = os.getcwd()
USER_NAME = getpass.getuser()

DOWNLOAD_FOLDER = f'C:\\Users\\{USER_NAME}\\Downloads\\'

FILE_NAME = 'FMS Franchisee Management System Invoice Details'
FILE_NAME_len = len(FILE_NAME)
EXTENSION = '.xlsx'
INVOICE_FILE = FILE_NAME + EXTENSION


def clear_screen():
    _ = os.system('cls')


def make_dir(folder_name, path=BASE_DIR):
    try:
        os.makedirs(os.path.join(path, folder_name))
    except:
        print(f"Folder Named '{folder_name}' Already Exists")


def newest_file(path):
    a = os.listdir(path)
    files = []
    for i in a:
        if FILE_NAME == i[0:FILE_NAME_len]:
            files.append(i)
    paths = [os.path.join(path, basename) for basename in files]
    return(max(paths, key=os.path.getctime))


file_name = newest_file(DOWNLOAD_FOLDER)
sheet = opensheet(file_name)
folder_name = 'Bill\\'+sheet.cell_value(1, 7) 


def bill_gen(tel_num=None):
	a = 1
	make_dir(folder_name, 'Bills')
	create_json(file_name, 0, folder_name, 0)
	snc_obj = open('data\\TVLSNC.json')
	vki_obj = open('data\\TVLVKI.json')
	bill_obj = open('data\\'+folder_name + '.json')
	SNC = json.loads(snc_obj.read())
	VKI = json.loads(vki_obj.read())
	bill = json.load(bill_obj)
	def get_details(tel_num):
		dic = {}
		dic['bill_date'] = bill[tel_num]['INVC DATE']
		dic['ex_code'] = bill[tel_num]['EXG CODE']
		dic['account_no'] = str(bill[tel_num]['BILL ACCNT NO'])
		dic['invoice_no'] = bill[tel_num]['INVC_NO']
		dic['mobile'] = str(bill[tel_num]['MOBILE'])
		dic['phone_no'] = bill[tel_num]['PHONE NO']
		dic['email'] = bill[tel_num]['EMAIL']
		dic['invoice_date'] = bill[tel_num]['INVC DATE']

		if bill[tel_num]['INVC AMT'] > bill[tel_num]['DUE AMT']:
		    dic['bill_amt'] = str(bill[tel_num]['INVC AMT'])
		else:
		    dic['bill_amt'] = str(bill[tel_num]['DUE AMT'])

		if dic['ex_code'] == 'TVLSNC':
		    dic['name'] = SNC[tel_num[6:]]['NAME']
		elif dic['ex_code'] == 'TVLVKI':
		    dic['name'] = VKI[tel_num[6:]]['NAME']

		return(dic)

	if tel_num != None and tel_num != '':
		try:
			data = get_details(tel_num)
			# name = 
			bill_amt = data['bill_amt']
			remarks = data['phone_no'],data['ex_code'],data['name']
			# ex_code = 
			url = f'upi://pay?pa=8015031422@upi&pn=Mr RAMKARTHICK  A&am={bill_amt}&cu=INR&mode=02&purpose=00&tn={remarks}&orgid=189999&sign=MEYCIQDpxyg4CEMWKXoPjnWZENthh+yQojdxIynSvypTaLHKCAIhALCrEbAk9WwVl68joptBwh+Hnm3JcDbp7MsrObwdfR2J'
		
			try:
				qr = qr_gen(url)
			except:
				print(' qrgen failed')
			# try:
			# 	invoice_write(data, 'temp.png')
			# 	print(data['phone_no'])
			# except:
			# 	print('img write faled')

		except:
			print('p')
		invoice_write(data, 'temp.png')
	elif tel_num == None or tel_num == '':
		for tel_num in bill:
			try:
				data = get_details(tel_num)
				# name = 
				bill_amt = data['bill_amt']
				remarks = data['phone_no'],data['ex_code'],data['name']
				# ex_code = 
				url = f'upi://pay?pa=8015031422@upi&pn=Mr RAMKARTHICK  A&am={bill_amt}&cu=INR&mode=02&purpose=00&tn={remarks}&orgid=189999&sign=MEYCIQDpxyg4CEMWKXoPjnWZENthh+yQojdxIynSvypTaLHKCAIhALCrEbAk9WwVl68joptBwh+Hnm3JcDbp7MsrObwdfR2J'
			
				try:
					qr = qr_gen(url)
				except:
					print(' qrgen failed')
				try:
					invoice_write(data, 'temp.png')
					print(data['phone_no'])
				except:
					print('img write faled')
			except:
				print('p')


if __name__ == '__main__':
	pass
