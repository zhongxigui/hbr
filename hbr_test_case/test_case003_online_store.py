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

class online_store(unittest.TestCase,object):
    def setUp(self):
        self.logger = logger(os.path.basename(__file__))
        start_App.setUp(self)
        time.sleep(3)
    def tearDown(self):
        start_App.tearDown(self)

    '''发布厂房'''
    def test01(self):
        time.sleep(5)
        startMethod.landing(self,17603031220,123456,8888)
        startMethod.element_location(self,By.ID,tabbar['网店坐标id'],2)
        startMethod.action_Id(self,Shop['添加按钮id'],'click')
        startMethod.action_Xpath(self,Shop['添加厂房xp'],'click')
        titleMethod.Photo(self,2)
        startMethod.action_Id(self,Shop['标题id'],titleMethod.duQu_Exlce(self,'其他',1,0))
        startMethod.action_Id(self,Shop['区域id'],'click')
        startMethod.action_Xpath(self,Shop['区域-其他城市xp'],'click')
        startMethod.action_Xpath(self,Shop['南京市xp'], 'click')
        startMethod.action_Xpath(self,Shop['玄武xp'], 'click')
        startMethod.action_Xpath(self,Shop['梅园xp'], 'click')
        startMethod.action_Id(self,Shop['厂房结构id'],'click')
        startMethod.action_Xpath(self,Shop['标准厂房xp'], 'click')
        startMethod.action_Id(self,Shop['楼层id'], 'click')
        startMethod.action_Xpath(self,Shop['一楼xp'],'click')
        startMethod.action_Id(self,Shop['新旧程度id'], 'click')
        startMethod.action_Xpath(self,Shop['新厂xp'],'click')
        startMethod.action_Id(self,Shop['租赁类别id'], 'click')
        startMethod.action_Xpath(self,Shop['租xp'], 'click')
        startMethod.action_Xpath(self,Shop['下一步xp'],'click')
        startMethod.action_Xpath(self,Shop['总面积xp'],titleMethod.duQu_Exlce(self,'其他',2,0))
        startMethod.action_Xpath(self,Shop['厂房价格xp'],'click')
        startMethod.action_Xpath(self,Shop['面议xp'], 'click')
        startMethod.action_Xpath(self,Shop['确定xp'], 'click')
        startMethod.action_Xpath(self,Shop['厂房概况xp'],titleMethod.duQu_Exlce(self,'其他',3,0))
        startMethod.action_Xpath(self,Shop['发布xp'],'click')
        startMethod.action_Xpath(self,Shop['确定xp'],'click')
        try:
            titleMethod.find_toast(self,'成功')
            self.assertEqual(1, 1, msg='发布成功')
        except:
            self.assertEqual(1, 2, msg='发布失败')


    '''删除厂房'''
    def test02(self):
        time.sleep(5)
        startMethod.element_location(self, By.ID, tabbar['网店坐标id'], 2)
        startMethod.element_location(self,By.ID,Shop['厂房图片id'],0)
        startMethod.action_Xpath(self,Shop['更多xp'],'click')
        startMethod.action_Xpath(self,Shop['删除房源xp'], 'click')
        startMethod.action_Xpath(self,Shop['确定xp'], 'click')
        try:
            titleMethod.find_toast(self, '成功')
            self.assertEqual(1, 1, msg='发布成功')
        except:
            self.assertEqual(1, 2, msg='发布失败')














#添加Suite
def suite():
     #定义一个单元测试容器
    suiteTest = unittest.TestSuite()
    # suiteTest.addTest(online_store('test01'))
    suiteTest.addTest(online_store('test02'))

    return suiteTest




if __name__ == '__main__':
    '''我们在如果想要生成测试报告，那么一定要注意右键执行时选择的右键菜单，一定要当做文件执行，不要让编辑器当做用例执行'''
    #确定生成报告的路径
    pathCode = paths['上上一级'] + '\hbr\hbr_test_result\\'
    curtime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    report_path = pathCode + curtime + 'test_case003'+'.html'
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