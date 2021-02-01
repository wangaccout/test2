import xlrd
import xlwt
import xlutils.copy

def GreatExcel(path, row,col):
    excel_book = xlwt.Workbook(encoding='utf-8')
    excel_book_sheet = excel_book.add_sheet('first_sheet', cell_overwrite_ok=False)
    for each_row in range(len(row)):
        excel_book_sheet.write(0, each_row, row[each_row])
    for each_col in range(len(col)):
        excel_book_sheet.write(each_col + 1, 0, col[each_col])
    excel_book.save(path)
    return excel_book

def ExchangeExcel(path, col):
    book = xlrd.open_workbook(path)
    exchange_excel_book = xlutils.copy.copy(book)
    exchange_excel_sheet = exchange_excel_book.get_sheet(0)
    for each_row in range(len(col)):
        exchange_excel_sheet.write(each_row + 1, 1, col[each_row])
    exchange_excel_book.save(path)

if __name__ == '__main__':
    path = 'D:\PyCharm\PyCharm Community Edition 2020.2\project\\test\\demo2.xls'
    first_row = ['各省市', '工资性收入', '家庭经营纯收入', '财产性收入', '转移性收入', '食品', '衣着',
           '居住', '家庭设备及服务', '交通和通讯', '文教、娱乐用品及服务', '医疗保健', '其他商品及服务']
    first_col = ['北京市', '天津市', '河北省', '山西省', '内蒙古自治区', '辽宁省','吉林省', '黑龙江省',
                    '上海市', '江苏省', '浙江省', '安徽省', '福建省','江西省', '山东省', '河南省', '湖北省',
                    '湖南省', '广东省', '广西壮族自治区','海南省', '重庆市', '四川省', '贵州省', '云南省',
                    '西藏自治区', '陕西省', '甘肃省', '青海省', '宁夏回族自治区', '新疆维吾尔自治区']
    second_col = ["418","96","487","115","100","188","138","107","161","115","418","96","487","115","100","188"]

    GreatExcel(path, first_row, first_col)
    ExchangeExcel(path, second_col)










