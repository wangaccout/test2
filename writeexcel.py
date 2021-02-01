import xlwt
import xlrd
import xlutils.copy

excel_path = 'D:\PyCharm\PyCharm Community Edition 2020.2\project\\test\\demo1.xls'
# 创建一个Workbook对象，相当于创建了一个Excel文件
excel_book = xlwt.Workbook(encoding='utf-8', style_compression=0)
# 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格
excel_sheet = excel_book.add_sheet('test', cell_overwrite_ok=True)
# 向表中添加数据方式1
excel_sheet.write(0, 0, "各省市")  # 0行0列写入 各省市
excel_sheet.write(0, 1, '工资收入')
# 向表中添加数据方式2
text1 = '北京'
excel_sheet.write(1, 0, text1)
text2 = '5000'
excel_sheet.write(1, 1, text2)


# 按行或列方式向工作表中添加数据
excel_sheet2 = excel_book.add_sheet('test2', cell_overwrite_ok=True)
project = ['各省市', '工资性收入', '家庭经营纯收入', '财产性收入', '转移性收入', '食品', '衣着',
           '居住', '家庭设备及服务', '交通和通讯', '文教、娱乐用品及服务', '医疗保健', '其他商品及服务']

for i in range(0, len(project)):
    excel_sheet2.write(0, i, project[i])
excel_book.save(excel_path)

province = ['北京市', '天津市', '河北 省', '山西省', '内蒙古自治区', '辽宁省',
            '吉林省', '黑龙江省', '上海市', '江苏省', '浙江省', '安徽省', '福建省',
            '江西省', '山东省', '河南省', '湖北省', '湖南省', '广东省', '广西壮族自治区',
            '海南省', '重庆市', '四川省', '贵州省', '云南省', '西藏自治区', '陕西省', '甘肃省',
            '青海省', '宁夏回族自治区', '新疆维吾尔自治区']
count = 0
while count < len(province):
    excel_sheet2.write(count+1, 0, province[count])
    count += 1
excel_book.save(excel_path)  # 保存Excel

# 使用xlutils修改Excel
excel_path1 = 'D:\PyCharm\PyCharm Community Edition 2020.2\project\\test\\demo.xls'
excel = xlrd.open_workbook(excel_path1, formatting_info=True)
new_book = xlutils.copy.copy(excel)
new_sheet = new_book.get_sheet(2)
new_sheet.write(0, 0, 'ok')
new_book.save(excel_path1)


























