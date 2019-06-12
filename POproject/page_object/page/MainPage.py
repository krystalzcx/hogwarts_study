
from selenium.webdriver.common.by import By

from page_object.page.BasePage import BasePage
from page_object.page.ProfilePage import ProfilePage
from page_object.page.QuotationPage import QuotationPage
from page_object.page.Searchpage import SearchPage
from page_object.page.SelectedPage import SelectedPage



'''
首页封装
'''


class MainPage(BasePage):
    _profile_button = (By.ID,"user_profile_icon")
    _searche_button = (By.ID,'home_search')

    #进入到首页之后选择自选，进入自选页面
    def gotoSelected(self):
        #调用全局的driver对象使用webdriver api定位操纵app

        zixuan='自选'
        self.findByText(zixuan)
        self.findByText(zixuan).click()
        return SelectedPage()

    #进入行情页
    def gotoQuotation(self):
        quotation = '行情'
        self.findByText(quotation)
        self.findByText(quotation).click()
        return QuotationPage()

    #进入搜索页
    def gotoSearch(self)->SearchPage:
        self.find(self._searche_button).click()
        return SearchPage()

    def gotoProfile(self):
        #self.find(self._profile_button).click()
        self.loadSteps("../data/MainPage.yaml", "gotoProfile")
        return ProfilePage()














