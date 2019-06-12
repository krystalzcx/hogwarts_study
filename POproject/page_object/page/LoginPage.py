from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_object.page.BasePage import BasePage
from selenium.webdriver.support import expected_conditions

#from page_object.page.Mainpage import MainPage.yaml

'''
登陆入口页
'''
class LoginPage(BasePage):
    #关闭登陆页按钮(两个都是页面左上角的叉按钮，但是在不同的页面开发起了不同的名字)
    _close_locator = (By.ID, "iv_close")
    _close2_locator = (By.ID, "iv_action_back")
    #以上两个back方式结合
    _back_locator = (By.XPATH, "//*[contains(@resource-id, 'iv_close') or contains(@resource-id, 'iv_action_back')]")

    #手机及其他登陆
    _other_locator = (By.ID, "tv_login_by_phone_or_others")
    #验证码快捷登陆:手机号
    _register_phone_number = (By.ID, "register_phone_number")
    #验证码快捷登陆:验证码
    _register_code = (By.ID, "register_code")
    #登陆按钮
    _button_next = (By.ID, "button_next")
    #邮箱手机号密码登陆
    _tv_login_with_account = (By.ID, "tv_login_with_account")
    #账号
    _login_account = (By.ID, "login_account")
    #密码
    _login_password = (By.ID, "login_password")
    #登陆失败后的提示框
    _error_msg = (By.ID, "md_content")

    #微信登录
    def loginByWX(self):
        return self

    #手机验证码登陆
    def loginByMSG(self, phone, code):
        return self


    #账号密码登陆方式
    #登陆失败
    def loginByPassword(self, account, password):
        # self.find(self._other_locator).click()
        # self.find(self._tv_login_with_account).click()
        # self.find(self._login_account).send_keys(account)
        # self.find(self._login_password).send_keys(password)
        # self.find(self._button_next).click()

        #从yaml加载数据
        #变量名var1、var2是变量名，是需要传入yaml文件的
        self.loadSteps("../data/LoginPage.yaml", "loginByPassword",var1=account,var2=password)
        return self

    # 账号密码登陆方式
    # 登陆成功
    #此处我们先不做处理
    def loginSuccessByPassword(self, account, password):
        #延迟导入
        from page_object.page.MainPage import MainPage
        return MainPage()

    def back(self):
        self.find(self._back_locator).click()
        # WebDriverWait(self.driver, 2).until(expected_conditions.presence_of_element_located(self._close_locator))
        from page_object.page.ProfilePage import ProfilePage
        return ProfilePage()

    def getErrorMsg(self):
        msg = self.find(self._error_msg).text
        self.findByText("确定").click()
        return msg






