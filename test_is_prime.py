import isPrime
import unittest
import requests

class Is_prime(unittest.TestCase):
    def setUp(self):
        print('测试开始')

    def test_is_prime(self):
        self.assertTrue(isPrime.is_prime(97), msg='is not prime')

    def test_is_in_case(self):
        a = 'hello'
        b = 'hello world'
        self.assertIn(a, b, msg='a is not in b')

    def test_response_case(self):
        method = 'get'
        url = 'http://www.baidu.com/'
        response = requests.request(method=method, url=url)
        response.encoding = 'utf-8'
        response_txt = response.text
        self.assertIn('百度一下555', response_txt, msg='百度主页打开错误')
    def tearDown(self):
        print('测试结束')

if __name__ == '__main__':
    unittest.main()
