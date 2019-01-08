# -*- coding:utf-8 -*-
from startAPP import *
from hbr_test_method.method import *
import unittest,requests,time
from hbr_test_conf.hbr_test_env.hbr_test_config import *
import HTMLTestReportCN
import smtplib
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart


def setUpModule():
    os.system('start startAppiumServer.bat')  # 启动appium服务
    time.sleep(8)  # 等待appium服务启动完毕
    print("test module star >>>>>>>>>>>>>>")
def tearDownModule():
    os.system('start stopAppiumServer.bat') #关闭appium服务
    print("test module end >>>>>>>>>>>>>>")



class Test_login(unittest.TestCase,object):
    def setUp(self):
        self.logger = logger(os.path.basename(__file__))
        start_App.setUp(self)
        time.sleep(3)
    def tearDown(self):
        start_App.tearDown(self)

    def test01(self):
        self.logger.info('*************************************************************')
        startMethod.landing(self, 17603031220, 1234, 8888)
        time.sleep(3)
        self.driver.tap(tabbar['我的坐标'], 100)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='添加盘源']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='租赁']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='厂房']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='扫楼']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='标准厂房']").click()
        startMethod.action_Id(self, business['返回id'], 'click')
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='确定']").click()
        time.sleep(3)
        try:
            WebDriverWait(self, 2).until(lambda driver: self.driver.find_element_by_xpath("//android.widget.TextView[@text='首页']"))
            self.assertEqual(1, 1, msg='登陆成功')
        except:
            self.assertEqual(1, 2, msg='登陆失败')

        startMethod.logout(self)


    def test02(self):
        self.logger.info('*************************************************************')
        startMethod.landing(self, 17603031220, 1234, 8888)
        self.logger.info('登录成功')
        time.sleep(3)
        self.driver.tap(tabbar['业务坐标'], 100)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='报备客户']").click()
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='请输入客户姓名']").set_text('林中')
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='请输入客户手机号码']").set_text('17554525425')
        startMethod.action_Id(self,business['性别id'],'click')
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='请选择客户行业']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='电子']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='互联网/电子商务']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='请选择客户来源']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='固定广告']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='提交']").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='厂房']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='A']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='租']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='30元/㎡·月以下']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='请选择需求区域']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='深圳市']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='全深圳市']").click()
        startMethod.action_Id(self,business['提交id'], 'click')
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='实业客(租)']").click()
        titleMethod.toachSweip(self, 0.5, 0.9, 0.5, 0.2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='半佣']").click()
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='请输入最小需求面积']").set_text('1000')
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='请输入最大需求面积']").set_text('10000')
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='否']").click()
        startMethod.action_Id(self, business['提交id'], 'click')
        time.sleep(5)
        startMethod.action_Id(self, business['返回id'], 'click')
        startMethod.logout(self)


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
    pathCode ='C:\\Users\\57874\\Desktop\\hbr\\hbr_test_result\\'
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
    smtpMethod.smtp_mail('qq', '578740769@qq.com', '36694640@qq.com')
