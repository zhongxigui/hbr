# coding:utf-8
import  unittest,requests,HTMLTestReportCN,time,os
from appium import webdriver
from  hbr_test_method.method import *
import smtplib
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart
PATH = lambda  p:os.path.abspath(
       os.path.join(os.path.dirname(__file__),p)
)
print(PATH)

def allCase():
    #待执行用例的目录
    case_dir=r'../hbr_test_case'
    #构造测试集合
    #suite=unittest.TestSuite()
    #获取到一个list集合
    allTest = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)
    #pattern————匹配脚本名称规则，test*.py是匹配所有test开头的所有脚本
    #top_level_dir 这个是顶层目录的名称 ，一般为空就可以了
    return  allTest

if __name__=="__main__":
    '''我们在如果想要生成测试报告，那么一定要注意右键执行时选择的右键菜单，一定要当做文件执行，不要让编辑器当做用例执行'''
    #确定生成报告的路径
    pathCode = paths['上上一级'] + '\hbr\hbr_test_result\\'
    curtime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    report_path = pathCode + curtime + 'test_caseall'+'.html'
    report_set = open(report_path, 'wb')

    #生成报告的Title,描述
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=report_set,
        title='自动化测试报告',
        description='详细测试用例结果',
        tester='zhong'
        )
    #运行测试用例
    runner.run(allCase())
    # 关闭文件，否则会无法生成文件
    report_set.close()
    smtpMethod.smtp_mail('qq', '578740769@qq.com', '36694640@qq.com')