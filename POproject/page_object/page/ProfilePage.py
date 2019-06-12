
from page_object.page.BasePage import BasePage
from page_object.page.LoginPage import LoginPage

'''
个人信息页(我的)
'''


class ProfilePage(BasePage):
    def gotoLogin(self):
        #self.findByText("点击登录").click()
        self.loadSteps("../data/ProfilePage.yaml","gotoLogin")
        return LoginPage()