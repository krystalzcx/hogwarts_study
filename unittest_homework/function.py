#coding:utf-8
#python3
import random
import string


'''
计算器
参数：
需要计算的数字：num_one,num_two
需要计算的符号：symbol
'''

def calculator(num_one,symbol,num_two):
    sum = 0
    if type(num_one) == str or type(num_two) == str:
        #print("字符串不能做数学计算")
        sum = "字符串不能做数学计算"
    else:
        if symbol == "+":
            sum = num_one + num_two
        elif symbol == "-":
            sum = num_one - num_two
        elif symbol == "*":
            sum = num_one * num_two
        elif symbol == "/":
            if num_two != 0:
                sum = num_one / num_two
            else:
                #print("除数不能为0")
                sum  = "除数不能为0"
        else:
            #print("只能计算加减乘除！")
            sum = "只能计算加减乘除!"
    return sum

'''
字符串大小写转换
parameter:需要转换的字符串
type:值可以为upper和lower
'''
def conversion_string(parameter,form):

    if type(parameter) == str:
        if form == "upper":
            parameter = parameter.upper()
        elif form == "lower":
            parameter =parameter.lower()
        else:
            print("只能输入upper(转为大写)或者lower(转为小写)两种类型")
    else:
        print("只有字符串才能进行大小写转换")

    return parameter


'''
随机生成字符串
lenth:随机字符串的长度
'''
def random_string(lenth):
    ran_str = ""
    if type(lenth) == str:
        print("输入的字符串的长度需要是正整数")
    elif lenth > 0 and type(lenth) == int:
        #字符串的内容包含字母和数字
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, lenth))
    else:
        print("输入的字符串的长度需要是正整数")
    return ran_str

