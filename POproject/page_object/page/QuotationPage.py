from appium.webdriver.common.touch_action import TouchAction

from page_object.driver.Client import AndroidClient
from page_object.page.BasePage import BasePage

'''
作业1:
行情页
'''
class QuotationPage(BasePage):
    def getIndexByName(self,name):
        # 提示totast
        # 有时存在有时不存在，可能需要按照坐标点击
        if self.driver.find_element_by_id("//*[contains(@resource-id,'snb_tip_text')]"):
            action = TouchAction(self.driver)
            action.press(x=500, y=500).release().perform()
        indexofQuotation = self.driver.find_element_by_xpath("//*[contains(@resource-id,index_name) and @text='"+name+"']"
         "/..//*[contains(@resource-id,'index_price')]").text
        return float(indexofQuotation)