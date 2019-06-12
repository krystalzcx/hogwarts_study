#
import pytest

from page_object.page.App import App


class TestLogin(object):
    @classmethod
    def setup_class(cls):
        cls.profilePage=App.main().gotoProfile()


    def setup_method(self):
        self.loginPage=self.profilePage.gotoLogin()


    @pytest.mark.parametrize("user,pw,msg",[
        ("156005347600", "111111", "手机号码"),
        ("15600534760", "111111", "密码错误")
    ])
    def test_login_password(self,user,pw,msg):
        self.loginPage.loginByPassword(user,pw)
        #获取的是提示弹框里的文字
        assert msg in self.loginPage.getErrorMsg()


    def teardown_method(self):
        #必须有setup_method()初始化进入登陆页对应，否则第二个用例进不去
        self.loginPage.back()