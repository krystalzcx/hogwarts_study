import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_object.driver.Client import AndroidClient
import yaml
#正则
import re


'''
封装driver
方便替换
'''
class BasePage():
    #黑名单
    element_black=[
        (By.XPATH,"ddd")
    ]
    driver:WebDriver
    def __init__(self):
        #把driver作为类级别变量
        #BasePage.driver = AndroidClient.driver
        #driver的类型不受限制
        self.driver = self.getDriver()

    @classmethod
    def getDriver(cls):
        cls.driver=AndroidClient.driver
        return cls.driver

    @classmethod
    def getClient(cls):
        return AndroidClient


    #多种类型查询方法
    # def find(self,kv)-> WebElement:
    #     #todo:处理各类弹框-老师会讲的
    #     #需要有返回值，否则find之后操作无法自动提示
    #     return self.find(*kv)

    def find(self,by,value):
        element:WebElement
        #加上重试机制(更加保险)
        for i in range(3):
            #try、except解决元素定位不到情况：页面没有缓存完、有弹框
            #处理弹框的两种方法：(1)找到页面的最顶层元素进行点击(2)黑名单
            try:
                element = self.driver.find_element(by,value)
                return element
            except:
                #找到页面的最顶层元素进行点击
                #黑名单机制：跳过弹框(通常黑名单足够)
                #self.driver.page_source
                #不抛异常的方式
                for e in BasePage.element_black:
                    elements = self.driver.find_elements(*e)
                    if(elements.__sizeof__()>0):
                        elements[0].click()



    #通过XPATH的text内容定位的方法
    def findByText(self,text)-> WebElement:
        return self.find((By.XPATH,"//*[@text='%s']"%text))

    #加载yaml文件
    #key：代表是那个方法，和po_path结合才能确定是哪个方法
    #**kwargs表示方法的传参数
    def loadSteps(self, po_path, key, **kwargs):
        #打开文件
        file = open(po_path,'r')
        #解析yaml文件
        po_data = yaml.load(file)
        #找到特定方法对应的数据
        po_math = po_data[key]
        po_elements=dict()
        #因为不止解析Loginpage.yaml文件，还有ProfilePage.yaml文件
        if po_data.keys().__contains__("elements"):
            po_elements =po_data['elements']
        #若elements不在一个文件内
        #po_elements=yaml.load(open('xxx.yaml'))['elements']

        for step in po_math:
            step:dict
            element_platform=dict()
            #判断yaml里某个key是否存在
            if step.keys().__contains__('element'):
                #获取yaml中elements里定位符和定位方式
                element_platform=po_elements[step['element']][AndroidClient.platform]
            else:
                element_platform={"by":step['by'],"locator":step['locator']}
            #找元素
            element:WebElement =self.find(by=element_platform["by"],value=element_platform["locator"])
            #分辨动作click和sendkey
            action = str(step["action"]).lower()
            #todo:定位失败，多是弹框，try catch后进入一个弹框处理(元素智能等待)
            if action == "click":
                element.click()
            elif action == "sendkeys":
                #step["text"]是yaml文件里"text"对应的值
                #若是传参数，那么step["text"]的值是形式如"$var"
                text = str(step["text"])
                #判断是否传参数，若传参数则将参数传入
                #k:key(变量名),v:value(变量值)
                for k,v in kwargs.items():
                    #正则表达式"$%s"
                    #v去替代的是k
                    text=text.replace("$%s" %k,v)
                    print("update text:%s" % (text))

                element.send_keys(text)
            else:
                print("UNKNOW COMMAND %s"% step)





















