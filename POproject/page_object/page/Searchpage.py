from selenium.webdriver.common.by import By

from page_object.page.BasePage import BasePage


'''
搜索页
首页进入搜索框，输入文字后进入搜索页
'''
class SearchPage(BasePage):
    #跨平台一般不推荐By.CLASS_NAME，因为此页面只有一个搜索框，所以不会定位到其他
    _edit_locator=(By.CLASS_NAME,"android.widget.EditText")

    #搜索框输入文字
    def search(self,key):
        self.find(self._edit_locator).send_keys(key)

        #搜索之后还是搜索页
        return self

    #添加搜索到的股票(添加到自选)
    def addToSelected(self,key):
        follow_button = (By.XPATH, "//*[contains(@resource-id, 'stockCode') and contains(@text,'%s')]/../../.." % key +
                         "//*[contains(@resource-id, 'follow_btn')]")
        self.find(follow_button).click()
        return self

    #移除已经关注的股票
    def removeFromSelected(self,key):
        followed_button = (By.XPATH, "//*[contains(@resource-id, 'stockCode') and contains(@text,'%s')]/../../.." % key +
                         "//*[contains(@resource-id, 'followed_btn')]")
        self.find(followed_button).click()
        return self

    #判断内容是否已经被添加
    #key非搜索的文字，对应的股票应该是唯一一个
    def isInSelected(self,key):
        #已选择的resourceId是followed_btn
        #未选择的resourceId是follow_btn
        #follow_button筛选的包含是'follow'，无论状态是已选择或者未选择的都会筛选出来
        #contains(@text,'%s')表示包含关键字就可以
        follow_button = (By.XPATH,"//*[contains(@resource-id, 'stockCode') and contains(@text,'%s')]/../../.." % key +
                         "//*[contains(@resource-id, 'follow')]")
        #获取筛选结果的resourceId
        id = self.find(follow_button).get_attribute("resourceId")
        #判断已经选择的是否在筛选结果里，包含选择True,不包含选择FALSE
        return "followed_btn" in id

    def cancel(self):
        self.findByText("取消").click()

    #查询用户
    def searchByUser(self,name):
        #作业2
        sear = self.search(name)
        yonghu = (By.XPATH,"//*[contains(@resource-id, 'ti_tab_indicator') ]//*[contains(@text,'用户')]")
        sear.find(yonghu).click()
        return self

    #添加用户
    def addUser(self,name):
        follow_button = (By.XPATH, "//*[contains(@resource-id, 'user_name') and contains(@text,'%s')]/../.." % name +
                         "//*[contains(@resource-id, 'follow_btn') and contains(@text,'关注')]")
        self.find(follow_button).click()
        return self

    #移除用户
    def removeUser(self,name):
        follow_button = (By.XPATH, "//*[contains(@resource-id, 'user_name') and contains(@text,'%s')]/../.." % name +
                         "//*[contains(@resource-id, 'followed_btn') and contains(@text,'关注')]")
        self.find(follow_button).click()
        return self

    #用户关注与否
    def isUserFollowed(self,name):
        #作业2
        follow_button = (By.XPATH, "//*[contains(@resource-id, 'user_name') and contains(@text,'%s')]/../.." % name +
                         "//*[contains(@resource-id, 'follow') and contains(@text,'关注')]")
        id = self.find(follow_button).get_attribute("resourceId")
        return "followed_btn" in id








