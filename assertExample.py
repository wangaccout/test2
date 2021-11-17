import unittest
class inputTest(unittest.TestCase):
    def setUp(self):
        # 用于测试用例执行前的初始化工作
        number = input('请输入一个数')
        self.number = int(number)  # 这个感觉跟 __init__里面的变量差不过

    def test_case1(self):
        self.assertEqual(self.number, 10, msg='your input is not 10')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

