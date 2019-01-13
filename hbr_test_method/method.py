import time
import random
import os
from appium.webdriver.common.touch_action import TouchAction #导入Touch Action类   这个是支持手势操作
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlrd #读取
from xlutils.copy import copy #复制写入
from hbr_test_conf.hbr_test_env.hbr_test_config import *
import smtplib
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart

class startMethod(object):
    '''ID获取元素'''
    def action_Id(self,id,text):
        if text=='obtain':
            pro = '获取元素：'
            self.logger.info(u'>>>%s%s' % (pro, id))
            return self.driver.find_element_by_id(id)
        else:
            if text=='click':
                pro = '点击控件：'
                self.logger.info(u'>>>%s%s' % (pro, id))
                return self.driver.find_element_by_id(id).click()
            else:
                pro = '输入内容为：'
                self.logger.info(u'>>>定位控件%s,%s%s' % (id,pro,text))
                return self.driver.find_element_by_id(id).set_text(text)

    '''xpath获取元素'''
    # def action_Xpath(self,xpath,text):
    #     if text=='obtain':
    #         pro = '获取元素：'
    #         self.logger.info(u'>>>%s%s' % (pro, xpath))
    #         return self.driver.find_element_by_xpath("//android.widget.TextView[@text='xpath']")
    #     else:
    #         if text=='click':
    #             pro = '点击控件：'
    #             self.logger.info(u'>>>%s%s' % (pro, xpath))
    #             return self.driver.find_element_by_xpath("//android.widget.TextView[@text='xpath']").click()
    #         else:
    #             pro = '输入内容为：'
    #             self.logger.info(u'>>>定位控件%s,%s%s' % (xpath,pro,text))
    #             return self.driver.find_element_by_xpath("//android.widget.TextView[@text='xpath']").set_text(text)

    '''登录方法'''
    def landing(self,usemame,password,verification):
        self.driver.find_element_by_id(login['账号id']).set_text(usemame)
        self.logger.info('输入账号为{}'.format(usemame))
        self.driver.find_element_by_id(login['密码id']).set_text(password)
        self.logger.info('输入密码为{}'.format(password))
        self.driver.find_element_by_id(login['登录按钮id']).click()
        self.driver.find_element_by_id(login['获取验证码id']).click()
        self.driver.find_element_by_id(login['输入验证码id']).set_text(verification)
        self.driver.find_element_by_id(login['验证码确定id']).click()

    '''退出登录'''
    def logout(self):
        self.driver.tap([(864, 1782), (1080, 1906)], 100)
        #self.driver.find_element_by_xpath("//android.widget.TextView[@text='我的']").click()  底部导航不行使用id xpath定位 暂时用tap
        titleMethod.toachSweip(self, 0.5, 0.9, 0.5, 0.2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='退出登录']").click()
        startMethod.action_Id(self, my['确认退出id'], 'click')





class titleMethod(object):
    '''excelb表格读取'''
    def duQu_Exlce(self,Sheet,a,b):
        exlce_Name = xlrd.open_workbook(paths['上上一级']+'\hbr\hbr_exlce_case\denglu_excel.xls')  # 打开excel文件格式为xlsx有的是xls
        table = exlce_Name.sheet_by_name(Sheet)
        cell_a1 = table.cell(a,b).value  # a代表行——从零开始   b代表列 从零开始
        return cell_a1
        self.logger.info(u'>>>获取excel表格内容：{}'.format(cell_a1))

    '''无限各方为滑动加载获取指定元素'''
    def scroll_my(self, x1, y1, x2, y2, xpathCode, timeOut):
        timeStart = time.strftime('%d%H%M%S', time.localtime())
        while 1:
            try:
                self.driver.find_element_by_xpath(xpathCode)
                self.logger.info('获取到指定元素')
                break
            except:
                action = TouchAction(self.driver)
                action.press(x=x1, y=y1).wait(ms=1000).move_to(x=x2, y=y2).release()
                action.perform()
                timeOver = time.strftime('%d%H%M%S', time.localtime())
                if int(timeOver) - int(timeStart) >= int(timeOut):
                    self.logger.debug('抓取指定元素超时，抓取时间为：%s' % (int(timeOver) - int(timeStart)))
                    break
                else:
                    continue
        return self.driver.find_element_by_xpath(xpathCode)

    '''一个滑动toach的方法'''
    def toachSweip(self,x,y,x1,y1):
        action = TouchAction(self.driver)
        action.press(x=x, y=y).wait(ms=1000).move_to(x=x1, y=y1).release()
        action.perform()









class smtpMethod(object):
    '''发送邮件'''
    @staticmethod
    def smtp_mail(choocemail, sendmail,receivemail):  # choocemail选择163还是qq,sendmail发件人，receivemail收件人

        #path = r"C:\\Users\\57874\\Desktop\\hbr\\hbr_test_result\\"
        path=paths['上上一级']+'\hbr\hbr_test_result\\'
        lists = os.listdir(path)
        filepath = path + lists[-1]
        with open(filepath, "rb") as fp:
            mail_body = fp.read()
        if choocemail == '163':  # 选择是163之后，所有的参数都是163的
            smtpserver = "smtp.163.com"  # 163邮箱服务器地址
            port = 0  # 端口号163邮箱为0，腾讯邮箱为 465 或者587
            mailtext = "您好:</br><p>　　　　请下载附件之后，由谷歌打开查看测试报告详情！</p>"  # 邮件内容
            mailCode = MIMEMultipart()
            # 使用MUMEText构造文本邮件字典
            mailCode['from'] = sendmail  # 添加发件人键值对
            mailCode['to'] = receivemail  # 添加收件人键值对
            mailCode['subject'] = '自动化测试报告'  # 添加文本主题键值对

            body = MIMEText(mailtext, "html", "utf-8")
            mailCode.attach(body)
            # 添加附件
            att = MIMEText(mail_body, "base64", "utf-8")
            att["Content-Type"] = "application/octet-stream"
            att["Content-Disposition"] = 'attachment; filename="test_report.html"'
            mailCode.attach(att)

            smtp = smtplib.SMTP()  # 使用该方法发送邮件
            smtp.connect(smtpserver)  # 链接服务器
            smtp.login(sendmail, 'qhjbbfqngrdsbfga')  # 登录
            smtp.sendmail(sendmail, receivemail, mailCode.as_string())  # 发送
            smtp.quit()  # 关闭
        if choocemail == 'qq':
            smtpserver = "smtp.qq.com"  # qq邮箱服务器地址
            port = 465
            mailtext = "您好:</br><p>　　　　请下载附件之后，由谷歌打开查看测试报告详情！</p>"  # 邮件内容
            mailCode = MIMEMultipart()

            mailCode['from'] = sendmail
            mailCode['to'] = receivemail
            mailCode['subject'] = '自动化测试报告'

            text = MIMEText(mailtext, 'html', 'utf-8')  # 构造邮件
            mailCode.attach(text)

            # 添加附件
            att = MIMEText(mail_body, "base64", "utf-8")
            att["Content-Type"] = "application/octet-stream"
            att["Content-Disposition"] = 'attachment; filename="report.html"'
            mailCode.attach(att)

        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sendmail, "qhjbbfqngrdsbfga")  # 登录
        smtp.sendmail(sendmail, receivemail, mailCode.as_string())  # 发送
        smtp.quit()  # 关闭

