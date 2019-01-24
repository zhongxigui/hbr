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

class address_list(unittest.TestCase,object):
    def setUp(self):
        self.logger = logger(os.path.basename(__file__))
        start_App.setUp(self)
        time.sleep(3)
    def tearDown(self):
        start_App.tearDown(self)

    '''搜索关注经纪人'''
    def test01(self):
        startMethod.landing(self,'17603031220','123456','8888')
        startMethod.action_Id(self,home['通讯录id'],'click')
        startMethod.action_Xpath(self,addresslist['请输入经纪人姓名短号xp'],'click')
        startMethod.action_Id(self,'com.zhaoshang800.partner:id/et_name','666')
        titleMethod.toachSweip(self, 0.5, 0.8, 0.5, 0.1)
        time.sleep(3)
        startMethod.element_location(self,By.XPATH,'//android.widget.TextView[@text=\'关注\']',2)
        time.sleep(3)
        titleMethod.Keycode(self,4)
        startMethod.action_Id(self,addresslist['我的关注id'],'click')


    '''搜索取消关注经纪人'''
    def test02(self):
        startMethod.action_Id(self, home['通讯录id'], 'click')
        startMethod.action_Xpath(self,addresslist['第一区域xp'],'click')
        self.driver.find_element_by_xpath('//android.widget.TextView[@text=\'福永一\']').click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text=\'宫震\']').click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text=\'关注\']').click()
        i=3
        while i > 0:
            startMethod.action_Xpath(self,commonality['返回id'],'click')
            i = i - 1
        startMethod.action_Id(self,addresslist['我的关注id'],'click')
        startMethod.element_location(self, By.XPATH, '//android.widget.TextView[@text=\'已关注\']', 0)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text=\'确定\']').click()
        titleMethod.toachSweip(self, 0.5, 0.1, 0.5, 0.8)











#添加Suite
def suite():
     #定义一个单元测试容器
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(address_list('test01'))
    suiteTest.addTest(address_list('test02'))
    return suiteTest




if __name__ == '__main__':
    '''我们在如果想要生成测试报告，那么一定要注意右键执行时选择的右键菜单，一定要当做文件执行，不要让编辑器当做用例执行'''
    #确定生成报告的路径
    pathCode = paths['上上一级'] + '\hbr\hbr_test_result\\'
    curtime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    report_path = pathCode + curtime + 'test_case002'+'.html'
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