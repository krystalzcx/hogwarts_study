from appium import webdriver
from appium.webdriver.webdriver import WebDriver
import yaml

'''
两个功能：安装APP、重启APP
返回一个全局变量driver
'''
class AndroidClient(object):

    #全局变量
    driver:WebDriver
    #默认值
    platform = 'android'
    @classmethod
    def install_app(cls) -> WebDriver:
        # caps = {}
        # #如果有必要，进行第一次安装
        # # caps["app"]=''
        # caps["platformName"] = "android"
        # caps["deviceName"] = "hogwarts"
        # caps["appPackage"] = "com.xueqiu.android"
        # caps["appActivity"] = ".view.WelcomeActivityAlias"
        # #解决第一次启动的权限问题
        # caps["autoGrantPermissions"] = "true"
        #
        # cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # cls.driver.implicitly_wait(10)
        # return cls.driver
        cls.initDriver("install_app")

    @classmethod
    def restart_app(cls) -> WebDriver:
        # caps = {}
        #
        # caps["platformName"] = "android"
        # caps["deviceName"] = "hogwarts"
        # caps["appPackage"] = "com.xueqiu.android"
        # caps["appActivity"] = ".view.WelcomeActivityAlias"
        # #为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态
        # caps['noReset']=True
        # caps['chromedriverExecutableDir']="/Users/seveniruby/projects/chromedriver/2.20"
        # caps['unicodeKeyboard']=True
        # caps['resetKeyboard']=True
        # #caps["udid"]="emulator-5554"
        #
        # cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # #全局(整个driver周期)隐式等待
        # cls.driver.implicitly_wait(10)
        # return cls.driver
        return cls.initDriver("restart_app")

    #初始化driver，数据驱动
    @classmethod
    def initDriver(cls,key):
        driver_data = yaml.load(open("../data/driver.yaml","r"))
        #获取平台类型
        platform = driver_data["platform"]
        #根据实际情况修改platform
        cls.platform=platform
        server = driver_data[key]['server']
        implicitly_wait = driver_data[key]['implicitly_wait']
        #根据上方获取的平台类型，再到yaml中获取平台对应的caps
        caps=driver_data[key]['caps'][platform]
        cls.driver = webdriver.Remote(server, caps)
        # 全局(整个driver周期)隐式等待
        cls.driver.implicitly_wait(implicitly_wait)
        return cls.driver




































