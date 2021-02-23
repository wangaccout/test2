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
        self.assertEqual(count.add(2), 11)
    def test_subtract_case(self):
        # count = add_count.Count(6, 3)
        self.assertEqual(count.subtract(), 3)
    def test_product_case(self):
        # count = add_count.Count(6, 3)
        self.assertEqual(count.product(), 18)
    def test_division_case(self):
        # count = add_count.Count(6, 3)
        self.assertEqual(count.division(), 3)
    def tearDown(self):
        print('测试结束')

if __name__ == '__main__':
    unittest.main()
