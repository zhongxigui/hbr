import os,re
#pc电脑路径
apkPath=r'D:\bao\prepartner.apk'
#直接获取设备名称
deviceName=re.findall('(.+?)\t',os.popen('adb devices').readlines()[1])[0]
#获取安卓版本号
platformVersion=''.join(re.findall('(.+?)',os.popen('adb shell getprop ro.build.version.release').readlines()[0]))
#获取安卓包名
#appPackage=re.findall('name=\'(.+?)\'',os.popen('aapt dump badging '+apkPath).readline())[0]
#获取appActivity
#appActivity=re.findall('launchable-activity: name=\'(.+?)\'',os.popen('aapt dump badging '+apkPath+'|findstr "activity"').readline())[0]


global config
config = {}
config['appiumPort']='4723'
config['bootStrapPort']=''
config['seldnroidPort']=''
config['chromiumPort']=''
config['platformName'] = 'Android'
config['platformVersion'] = platformVersion
config['deviceName'] = deviceName
config['appPackage'] ='com.zhaoshang800.partner'
#config['appActivity']=appActivity
config['appActivity']='com.zhaoshang800.partner.activity.WelcomeActivity'
config['noReset'] = True
config['unicodeKeyboard'] = True
config['resetKeyboard'] = True
config['automationName']= 'Uiautomator2'
config['app'] = apkPath
config['newCommandTimeout'] = '400'



'''登录页面'''
global login
login = {}
login['账号id']='com.zhaoshang800.partner:id/et_login_name'
login['密码id']='com.zhaoshang800.partner:id/et_login_word'
login['登录按钮id']='com.zhaoshang800.partner:id/btn_login'
login['获取验证码id']='com.zhaoshang800.partner:id/get_verification'
login['输入验证码id']='com.zhaoshang800.partner:id/verification'
login['验证码确定id']='com.zhaoshang800.partner:id/check_sure'


'''底部导航'''
global tabbar
tabbar = {}
tabbar['首页text']='首页'
tabbar['业务text']='业务'
tabbar['网店text']='网店'
tabbar['圈子text']='圈子'
tabbar['我的text']='我的'


'''首页界面'''
global home
home = {}
home['搜索栏id']='com.zhaoshang800.partner:id/home_search'


'''业务界面'''
global business
business={}
business['返回id']='com.zhaoshang800.partner:id/view_iv_back'
business['性别id']='com.zhaoshang800.partner:id/rb_man'
business['提交id']='com.zhaoshang800.partner:id/tv_submit'

'''我的界面'''
global my
my={}
my['设置text']='设置'
my['退出登录text']='退出登录'
my['确认退出id']='com.zhaoshang800.partner:id/tv_new_dialog_right'
