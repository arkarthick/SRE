import os
import json
import xlrd
# from invoice_gen import opensheet


BASE_DIR = os.getcwd()
file_path = 'D:\\Bsnl FTTH\\FTTH.xlsx'
ex_codes = ['TVLSNC', 'TVLVKI']


def opensheet(filepath, sheet_index=0):
    wb = xlrd.open_workbook(filepath)
    sheet = wb.sheet_by_index(sheet_index)
    sheet.cell_value(0, 0)  # For row 0 and column 0
    return sheet


def fetch_data(file_path, index, key_index=6):
    data = {}
    keys = None
    sheet = opensheet(file_path, index)
    for i in range(sheet.nrows):
        if i == 0:
            keys = sheet.row_values(i)
        elif sheet.cell_value(i, 2) != '':
            row_value = sheet.row_values(i)
            dic = {}
            for j in range(len(row_value)):
                if isinstance(row_value[j], float):
                    row_value[j] = int(row_value[j])

                dic[f'{keys[j]}'] = row_value[j]
            data[f'{row_value[key_index]}'] = dic

    return data


def create_json(file_path, sheet_index, filename, key_index):
    data = fetch_data(file_path, sheet_index, key_index)

    json_object = json.dumps(data, indent=4)

    with open(f"data\\{filename}.json", "w+") as outfile:
        outfile.write(json_object)
    # return json_object


def main():
    for i in range(len(ex_codes)):
        create_json(file_path=file_path, sheet_index=i,
                    filename=ex_codes[i], key_index=6)


if __name__ == '__main__':
    main()
