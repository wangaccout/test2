import xlwt
excel_path = 'D:\PyCharm\PyCharm Community Edition 2020.2\project\\test\\demo1.xls'
excel_book = xlwt.Workbook(encoding='utf-8', style_compression=0)
excel_sheet = excel_book.add_sheet('test', cell_overwrite_ok=True)