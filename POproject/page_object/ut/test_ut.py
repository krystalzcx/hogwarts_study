
'''
单元测试
测试yaml加载

'''

import yaml

class TestYaml(object):
    def test_yaml(self):
        #加载yaml文件
        dict=yaml.load(open("../data/MainPage.yaml", 'r'))
        print(dict)

        for step in dict["gotoProfile"]:
            print(step["locator"])