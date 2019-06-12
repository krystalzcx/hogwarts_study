from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from page_object.driver.Client import AndroidClient
from page_object.page.BasePage import BasePage

'''
自选页面封装
'''
class SelectedPage(BasePage):
    #进入自选后的默认页面(会改变)
    def addDefault(self):
        return self
    def gotoHS(self):
        self.findByText("沪深")
        return self

    #通过名字获取股票价格
    def getPriceByName(self,name)->float:
        #查看页面代码，通过股票name逐层往找上级，直到这个上级可以正好包含股票name对应的price

        priceLocator = (By.XPATH,"//*[contains(@resource-id,'stockName') and @text='%s']" %name+
        "/../../..//*[contains(@resource-id,'currentPrice')]")
        price = self.find(priceLocator).text
        return float(price)


