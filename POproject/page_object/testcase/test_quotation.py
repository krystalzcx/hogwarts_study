import pytest

from page_object.page.App import App
from page_object.page.MainPage import MainPage

'''
测试行情页用例
'''
class TestQuotation():
    #测试股票指数
    def test_index(self):
        assert App.main().gotoQuotation().getIndexByName("深证成指")>8000