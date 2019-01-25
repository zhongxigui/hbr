import os,re
#pc电脑路径
#apkPath=r'D:\bao\prepartner.apk'
apkPath=r'D:\bao\devpartner.apk'
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
#config['appPackage'] ='com.zhaoshang800.partner'
config['appPackage'] ='com.zhaoshang800.partner.debug'
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
login['账号id']=config['appPackage']+':id/et_login_name'
login['密码id']=config['appPackage']+':id/et_login_word'
login['登录按钮id']=config['appPackage']+':id/btn_login'
login['获取验证码id']=config['appPackage']+':id/get_verification'
login['输入验证码id']=config['appPackage']+':id/verification'
login['验证码确定id']=config['appPackage']+':id/check_sure'



'''底部导航'''
global tabbar
tabbar = {}
tabbar['首页坐标id']=config['appPackage']+':id/tv_tab_name'
tabbar['业务坐标id']=config['appPackage']+':id/tv_tab_name'
tabbar['网店坐标id']=config['appPackage']+':id/tv_tab_name'
tabbar['圈子坐标id']=config['appPackage']+':id/tv_tab_name'
tabbar['我的坐标id']=config['appPackage']+':id/tv_tab_name'



'''首页界面'''
global home
home = {}
home['搜索栏id']=config['appPackage']+':id/home_search'
home['通知公告xpath']='通知公告'
home['通讯录id']=config['appPackage']+':id/home_contacts'



'''通讯录'''
global addresslist
addresslist = {}
addresslist['请输入经纪人名字和/短号id']= config['appPackage']+':id/ll_broker_search'
addresslist['我的关注id']=config['appPackage']+':id/tv_my_follow'
addresslist['第一区域xp']='//android.widget.TextView[@text=\'第一区域\']'
addresslist['请输入经纪人姓名短号xp']='//android.widget.TextView[@text=\'请输入经纪人姓名/短号\']'
addresslist['请输入经纪人姓名短号1xp']='//android.widget.EditText[@text=\'请输入经纪人姓名/短号\']'



'''网店模块'''
global Shop
Shop = {}
Shop['添加按钮id']=config['appPackage']+':id/view_tv_right_text'
Shop['添加厂房xp']='//android.widget.TextView[@text=\'厂房\']'
Shop['添加写字楼xp']='//android.widget.TextView[@text=\'写字楼\']'
Shop['添加土地xp']='//android.widget.TextView[@text=\'土地\']'
Shop['厂房模块xp']='//android.widget.TextView[@text=\'厂房\']'
Shop['写字楼xp']='//android.widget.TextView[@text=\'写字楼\']'
Shop['土地xp']='//android.widget.TextView[@text=\'土地\']'
Shop['标题id']=config['appPackage']+':id/et_title'
Shop['区域id']=config['appPackage']+':id/tv_district_choose'
Shop['区域-其他城市xp']='//android.widget.TextView[@text=\'其他城市\']'
Shop['南京市xp']='//android.widget.TextView[@text=\'南京市\']'
Shop['玄武xp']='//android.widget.TextView[@text=\'玄武\']'
Shop['梅园xp']='//android.widget.TextView[@text=\'梅园\']'
Shop['北京xp']='//android.widget.TextView[@text=\'北京\']'
Shop['东城xp']='//android.widget.TextView[@text=\'东城\']'
Shop['东华门xp']='//android.widget.TextView[@text=\'东华门\']'
Shop['厂房结构id']=config['appPackage']+':id/tv_structure_choose'
Shop['标准厂房xp']='//android.widget.TextView[@text=\'标准厂房\']'
Shop['楼层id']=config['appPackage']+':id/tv_floor_choose'
Shop['一楼xp']='//android.widget.TextView[@text=\'一楼\']'
Shop['新旧程度id']=config['appPackage']+':id/tv_new_or_old_choose'
Shop['新厂xp']='//android.widget.TextView[@text=\'新厂\']'
Shop['租赁类别id']=config['appPackage']+':id/tv_type_choose'
Shop['租xp']='//android.widget.TextView[@text=\'租\']'
Shop['下一步xp']='//android.widget.TextView[@text=\'下一步\']'
Shop['总面积xp']='//android.widget.EditText[@text=\'例：2000\']'
Shop['厂房价格xp']='//android.widget.TextView[@text=\'请选择\']'
Shop['面议xp']='//android.widget.TextView[@text=\'面议\']'
Shop['确定xp']='//android.widget.TextView[@text=\'确定\']'
Shop['厂房概况xp']='//android.widget.EditText[@text=\'请勿输入手机号或华夏相关的信息，否则可能此条会被审核删除\']'
Shop['发布xp']='//android.widget.TextView[@text=\'发布\']'
Shop['确定xp']='//android.widget.TextView[@text=\'确定\']'
Shop['厂房图片id']=config['appPackage']+':id/iv_item_factory_logo'
Shop['更多xp']='//android.widget.ImageView[@index=\'2\']'
Shop['删除房源xp']='//android.widget.TextView[@text=\'删除房源\']'




'''业务模块'''
global business
business={}
business['添加盘源xp']='//android.widget.TextView[@text=\'添加盘源\']'
business['我的盘源xp']='//android.widget.TextView[@text=\'我的盘源\']'
business['搜索盘源xp']='//android.widget.TextView[@text=\'搜索盘源\']'
business['报备客户xp']='//android.widget.TextView[@text=\'报备客户\']'
business['我的客户xp']='//android.widget.TextView[@text=\'我的客户\']'
business['成交报告xp']='//android.widget.TextView[@text=\'成交报告\']'



'''我的界面'''
global my
my={}
my['设置text']='设置'
my['退出登录text']='退出登录'
my['确认退出id']=config['appPackage']+':id/tv_new_dialog_right'



'''路径'''
global paths
paths={}
paths['当前']=os.getcwd()
paths['上一级']=os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + ".")
paths['上上一级']=os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + "..")



'''公共按钮'''
global commonality
commonality={}
commonality['返回id']=config['appPackage']+':id/view_iv_back'
commonality['点击相机id']=config['appPackage']+':id/iv_pic_add'
commonality['选择相册xp']='//android.widget.TextView[@text=\'相册\']'
commonality['选择图片id']=config['appPackage']+':id/check_box'
commonality['完成id']=config['appPackage']+':id/album_menu_finish'
commonality['解锁封面xp']='//android.view.View[@index=\'2\']'
