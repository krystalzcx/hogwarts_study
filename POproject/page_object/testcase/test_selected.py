
import pytest

from page_object.page.App import App
from page_object.page.MainPage import MainPage

'''
测试自选页面用例
'''
class TestSelected(object):
    mainPage:MainPage

    #因为每个方法都要从首页进入，再到搜索页，所以把进入首页(包含程序重启)封装
    @classmethod
    def setup_class(cls):
        cls.mainPage=App.main()


    #测试股票价格
    def test_price(self):
        #首页实例化: App.main()
        #因为gotoSelected()返回的是类SelectedPage，所以可直接引用getPriceByName()
        assert self.mainPage.gotoSelected().gotoHS().getPriceByName("招商银行")==34.38























