import xl_to_json
import invoice_gen
import time
if __name__ == '__main__':
	while True:
		invoice_gen.clear_screen()
		var = input('''
if you want to update customer details type 'update-json'.
Type 'exit()' or press CTRL+c to Close the app
input telephone number with std code to get bill for one person
or press enter to get bill for all customers.
eg: 04633-29xxxx
>>>''')

		if var == 'update-json':
			xl_to_json.main()
		elif var == 'exit()':
			print('application is closing')
			time.sleep(3)
			break
		else:
			invoice_gen.bill_gen(var)