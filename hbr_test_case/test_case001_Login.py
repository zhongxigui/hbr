# -*- coding:utf-8 -*-
from startAPP import *
from hbr_test_method.method import *
import unittest,requests,time
from hbr_test_conf.hbr_test_env.hbr_test_config import *
import HTMLTestReportCN
import smtplib
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart
from ddt import ddt,data,file_data,unpack
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction #导入Touch Action类


# def setUpModule():
#     os.system('start startAppiumServer.bat')  # 启动appium服务
#     time.sleep(8)  # 等待appium服务启动完毕
#     print("test module star >>>>>>>>>>>>>>")
# def tearDownModule():
#     os.system('start stopAppiumServer.bat') #关闭appium服务
#     print("test module end >>>>>>>>>>>>>>")

@ddt
class Test_login(unittest.TestCase,object):
    def setUp(self):
        self.logger = logger(os.path.basename(__file__))
        start_App.setUp(self)
        time.sleep(3)
    def tearDown(self):
        start_App.tearDown(self)


    '''登录验证'''
    @file_data('D:\github\hbr\hbr_exlce_case\ddt_json.json')
    def test01(self,usemame,password,verification):
        self.driver.find_element_by_id(login['账号id']).set_text(usemame)
        self.logger.info('输入账号为{}'.format(usemame))
        self.driver.find_element_by_id(login['密码id']).set_text(password)
        self.logger.info('输入密码为{}'.format(password))
        self.driver.find_element_by_id(login['登录按钮id']).click()
        while 1==1:
            if titleMethod.find_toast(self,'请输入帐号或密码'):
                print('登录失败')
                break
            elif titleMethod.find_toast(self,'手机号码格式不正确，请联系助理'):
                print('登录失败')
                break
            elif titleMethod.find_toast(self,'手机号码不存在，请联系助理'):
                print('登录失败')
                break
            else:
                self.driver.find_element_by_id(login['获取验证码id']).click()
                self.driver.find_element_by_id(login['输入验证码id']).set_text(verification)
                self.driver.find_element_by_id(login['验证码确定id']).click()
                startMethod.logout(self)
                break

    def test02(self):
        pass


#添加Suite
def suite():
     #定义一个单元测试容器
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(Test_login('test01'))
    suiteTest.addTest(Test_login('test02'))
    return suiteTest




if __name__ == '__main__':
    '''我们在如果想要生成测试报告，那么一定要注意右键执行时选择的右键菜单，一定要当做文件执行，不要让编辑器当做用例执行'''
    #确定生成报告的路径
    pathCode = paths['上上一级'] + '\hbr\hbr_test_result\\'
    curtime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    report_path = pathCode + curtime + 'test_case001'+'.html'
    report_set = open(report_path, 'wb')

    #生成报告的Title,描述
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=report_set,
        title='自动化测试报告',
        description='详细测试用例结果',
        tester='zhong'
        )
    #运行测试用例
    runner.run(suite())
    # 关闭文件，否则会无法生成文件
    report_set.close()
    #smtpMethod.smtp_mail('qq', '578740769@qq.com', '36694640@qq.com')
