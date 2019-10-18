from appium import webdriver

def init_driver():
    desiredCaps = {}
    # 系统
    desiredCaps["platformName"] = 'Android'
    # 版本
    desiredCaps["platformVersion"] = '6.0.1'
    # 设备号
    desiredCaps["deviceName"] = 'b8faf065'
    # 包名
    desiredCaps["appPackage"] = 'com.het.bind.telecom'
    # 启动名
    desiredCaps["appActivity"] = '.ui.SplashActivity'
    # 中文输入允许
    desiredCaps['unicodeKeyboard'] = True
    desiredCaps['resetKeyboard'] = True
    # 声明手机驱动对象
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desiredCaps)
    return driver