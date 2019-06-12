
from page_object.driver.Client import AndroidClient
from page_object.page.BasePage import BasePage
from page_object.page.MainPage import MainPage

'''
APP初始化
'''
class App(BasePage):
    #重启APP即为进入首页
    @classmethod
    def main(cls):
        #driver的类型不受限制
        cls.getClient().restart_app()
        #重启之后仍然是首页
        return MainPage()