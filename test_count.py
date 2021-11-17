import add_count
import unittest

# 不使用框架编写的单元测试
# class test_count():
#     def test_add(self):
#         try:
#             count = add_count.Count(2, 3)
#             add = count.add(2)
#             assert(add == 8)
#         except AssertionError as Error_msg:
#             print(Error_msg.__class__.__name__)
#             print(Error_msg)
#         else:
#             print('test pass')
#
# test_case = test_count()
# test_case.test_add()

# 使用单元测试框架(Unittest)来写
count = add_count.Count(6, 3)
class test_count(unittest.TestCase):
    # count = add_count.Count(6, 3)
    def setUp(self):
        print('测试开始')
    def test_add_case(self):
        # count = add_count.Count(6, 3)
        print("测试加法")
        self.assertEqual(count.add(2), 11)
    def test_subtract_case(self):
        # count = add_count.Count(6, 3)
        print("测试减法")
        self.assertEqual(count.subtract(), 3)
    def test_product_case(self):
        # count = add_count.Count(6, 3)
        print("测试乘法")
        self.assertEqual(count.product(), 18)
    def test_division_case(self):
        # count = add_count.Count(6, 3)
        print("测试除法")
        self.assertEqual(count.division(), 2)
    def tearDown(self):
        print('测试结束')

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()  # 构造测试集，实例化一个测试集
    suite.addTest(test_count('test_division_case'))  # 添加测试用例
    # runner = unittest.TextTestRunner()  # 执行测试
    # runner.run(suite)
    # 将测试结果写入txt中
    with open('UnittestTextReport.txt', 'w') as UnittestTextReport:
        runner = unittest.TextTestRunner(stream=UnittestTextReport, verbosity=2)
        runner.run(suite)

'''第一个参数self是代表本类的意思
第二个参数stream是代表输出dao的测试报告路zhuan径，你这里stream=sys.stdout,即输出在shu控制台
第三个参数verbosity=2，显示用例打印内容
第四个参数title，表示测试报告标题
第五个参数description，表示测试报告的描述
第六个参数tester，表示测试人员名字，不传默认为QA'''