#from pandas import read_excel
import openpyxl

my_sheet = 'DATA'
file_name = 'Datalistsss.xlsx'
#df = read_excel(file_name, sheet_name = my_sheet)
#print(df.head())

wb = openpyxl.load_workbook(file_name)

sheet_names = wb.get_sheet_names()
print(sheet_names)

sheet = wb.get_sheet_by_name(my_sheet)
print(sheet)
