import os
import xlrd
from time import strftime, sleep
import getpass
from tkinter import *
from functools import partial


BASE_DIR = os.getcwd()
USER_NAME = getpass.getuser()

Download_folder = f'C:\\Users\\{USER_NAME}\\Downloads\\'

INVOICE_FILE = 'FMS Franchisee Management System Invoice Details.xlsx'


def clear_screen():
	_ = os.system('cls')

def make_dir(folder_name, path=BASE_DIR):
	if path[-1]!='/' or path[-1] != '\\':
		path = path+'\\'
	try:
		os.makedirs(path+folder_name)
	except:
		pass
	# try:
	# 	os.chdir(BASE_DIR+'/'+folder_name)
	# except:
	# 	pass

def listdir(path):
	'''this fi=unc will change the dir to the
	inputed path and list out the files in the directory'''
	try:
		os.chdir(path)
		files = os.listdir()
		return files
	except:
		pass

def open_sheet(filename, path, sheet_index=0):
	os.chdir(path)
	book = xlrd.open_workbook(filename)
	sheet = book.sheet_by_index(sheet_index)
	sheet.cell_value(1,1)
	return sheet



#---------Tkinter-------------
window =Tk()

#---properties---
window.title('SRE Bill Generator')
window.geometry('400x300')
window.resizable(False, False)

#---btn---
def printo(name, telephone, ammount, tax, rad_taxadded):
	name = name.get()
	telephone = telephone.get()
	ammount = ammount.get()
	rad_taxadded = rad_taxadded.get()
	tax = tax.get()
	if tax =='':
		tax='18'

	a = int(ammount)*(1+(int(tax)/100))
	print(name, telephone, ammount, a, rad_taxadded)

#---contents---

lbl_name = Label(window, text='Name')
name = Entry(window)
lbl_telephone = Label(window, text='Telephone')
telephone = Entry(window)

lbl_bildate = Label(window, text='Bill Date')
date = Entry(window)
lbl_bilno = Label(window, text='Bill No.')
bill_no = Entry(window)

lbl_bilamt = Label(window, text='Bill Ammount')
bill_ammount = Entry(window)
lbl_tax = Label(window, text='Tax')
tax = Entry(window)

rad_taxadded = Checkbutton(window, text='with tax')
rad_taxadded.grid(row=3, column=0)



lbl_name.grid(row=0, column=0)
name.grid(row=0, column=1)
lbl_telephone.grid(row=0, column=2)
telephone.grid(row=0, column=3)

lbl_bildate.grid(row=1, column=0)
date.grid(row=1, column=1)
lbl_bilno.grid(row=1, column=2)
bill_no.grid(row=1, column=3)

lbl_bilamt.grid(row=2, column=0)
bill_ammount.grid(row=2, column=1)
lbl_tax.grid(row=2, column=2)
tax.grid(row=2, column=3)
	

bill_ammount.insert(0, '2500')
telephone.insert(0, '04633')
tax.insert(0,18)

data=partial(printo, name, telephone, bill_ammount, tax, rad_taxadded)
#--btns--
btn = Button(text='click', command=data).grid(column=3, row=10)

if __name__ == '__main__':
	window.mainloop()