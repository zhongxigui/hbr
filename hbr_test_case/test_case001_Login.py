# -*- coding:utf-8 -*-
from startAPP import *
from hbr_test_method.method import *
import unittest,requests,time
from hbr_test_conf.hbr_test_env.hbr_test_config import *
import HTMLTestReportCN
import smtplib
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart


# def setUpModule():
#     os.system('start startAppiumServer.bat')  # 启动appium服务
#     time.sleep(8)  # 等待appium服务启动完毕
#     print("test module star >>>>>>>>>>>>>>")
# def tearDownModule():
#     os.system('start stopAppiumServer.bat') #关闭appium服务
#     print("test module end >>>>>>>>>>>>>>")



class Test_login(unittest.TestCase,object):
    def setUp(self):
        self.logger = logger(os.path.basename(__file__))
        start_App.setUp(self)
        time.sleep(3)
    def tearDown(self):
        start_App.tearDown(self)

    def test01(self):
        self.logger.info('正常登录')
        startMethod.landing(self, 17603031220, 1234, 8888)
        startMethod.logout(self)

    def test02(self):
        self.logger.info('手机号不存在')
        startMethod.landing(self, 17603034420, 1234, 8888)

    def test03(self):
        self.logger.info('密码错误')
        startMethod.landing(self, 17603034420, 12314, 8888)

#添加Suite
def suite():
     #定义一个单元测试容器
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(Test_login('test01'))
    suiteTest.addTest(Test_login('test02'))
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
