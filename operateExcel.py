from openpyxl import load_workbook

wb = load_workbook('test.xlsx')
sheet = wb['A1']
res = sheet.cell(row=1,column=1).value
print(res)
print(sheet.max_column)
print(sheet.max_row)
