import xlrd


# 例1 通过Book.sheets()等方法获得sheet对象
excel_path = 'D:\PyCharm\PyCharm Community Edition 2020.2\project\\test\\demo.xls'
# 打开文件，获取Excel文件的workbook对象
excel = xlrd.open_workbook(excel_path, encoding_override='utf-8')
# 返回所有sheet对象的list
all_sheet = excel.sheets()
print(all_sheet)
# for each_sheet in all_sheet:
#     print(each_sheet)
#     print('sheet名称为：', each_sheet.name)
# print(excel.sheet_names())  # 获得的是一个str类型的列表（sheet对象名字的列表）
# print(excel.sheet_by_name('Sheet1'))  # 根据sheet名称输出
# print(excel.sheet_by_index(2))  # 根据索引输出
# print(excel.nsheets)  # 返回sheet数目

# 获取工作表信息
# sheet_name = []
# sheet_row = []
# sheet_col = []
# for sheet in all_sheet:
#     sheet_name.append(sheet.name)
#     print('该Excel共有{0}个sheet，当前sheet名称为{1}，该sheet共有{2}行{3}列'
#           .format(len(all_sheet), sheet.name, sheet.nrows, sheet.ncols))
#     sheet_row.append(sheet.nrows)
#     sheet_col.append(sheet.ncols)
# print(sheet_name, '\n', sheet_row, '\n', sheet_col)

# 按行方式获得工作表的数据
# for sheetRow in all_sheet:
#     print('当前sheet是：', sheetRow.name)
#     for each_row in range(sheetRow.nrows):
#         print(sheetRow.name, '的当前为%s行：' % each_row)
#         print(sheetRow.row_values(each_row))
#
# first_row_value = excel.sheet_by_name('Sheet2').row_values(0)  # 根据sheet名称打印指定的某一行
# print(first_row_value)

# 按列方式获得工作表的数据
# for sheetCol in all_sheet:
#     for each_col in range(sheetCol.ncols):
#         print('当前为%s列：' % each_col)
#         print(sheetCol.col_values(each_col))
# second_col_value = excel.sheet_by_index(1).col_values(1)
# print(second_col_value)

# 获取行或列对象，通过sheet对象中的sheet.row(r)或sheet.col(c)可以获得指定行或列，返回cell对象的list
# sheetr = excel.sheet_by_name('Sheet1').row(1)
# sheetc = excel.sheet_by_name('Sheet1').col(1)
# print(sheetr)
# print(sheetc)

# 获取某一个单元格的数据
# sheetrc = excel.sheet_by_name('Sheet1').cell(1, 1)
# print(sheetrc)
# sheet_cell_value = sheetrc.value  # 返回单元格的值
# print(sheet_cell_value)
# sheetrc1 = excel.sheet_by_name('Sheet1').cell(2, 1).value  # 根据位置获取单元格的值
# print(sheetrc1)

# 获取每一个单元格的数据
sheet = excel.sheets()[0]
sheet_row_mount = sheet.nrows
sheet_col_mount = sheet.ncols
print(sheet_row_mount, sheet_col_mount)
for x in range(sheet_row_mount):
    y = 0
    while y < sheet_col_mount:
        print(sheet.cell_value(x, y))
        y += 1










