#coding:utf-8
#python3
#from _pytest import unittest
'''
课程贴19047：作业1
'''

import function
import unittest

class Test_calculator(unittest.TestCase):

    #传入非数字(需要计算的两个数字)
    def test_case0_calculator_NoNumber(self):
        result = function.calculator("1","+","2")
        self.assertEqual(result,"字符串不能做数学计算")


    #不合法的计算符号
    def test_case_calculator_illegal_symbol(self):
        result = function.calculator(1,"&",3)
        self.assertEqual(result, "只能计算加减乘除!")



if __name__ == '__main__':
    unittest.main(verbosity=2)