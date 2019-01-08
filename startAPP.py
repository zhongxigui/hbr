from appium import webdriver
import logging,re,os
from hbr_test_conf.hbr_test_env.hbr_test_config import config
from hbr_test_log.hbr_test_logmethod import logger




class start_App(object):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = config['platformName']
        desired_caps['platformVersion'] = config['platformVersion']
        desired_caps['deviceName'] = config['deviceName']
        desired_caps['app'] = config['app']
        desired_caps['appPackage'] = config['appPackage']
        desired_caps['appActivity']=config['appActivity']
        desired_caps['noReset'] = config['noReset']
        desired_caps['unicodeKeyboard'] = config['unicodeKeyboard']
        desired_caps['resetKeyboard'] = config['resetKeyboard']
        desired_caps['automationName'] = config['automationName']
        desired_caps['newCommandTimeout'] =config['newCommandTimeout']
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
    def tearDown(self):
        self.driver.quit()