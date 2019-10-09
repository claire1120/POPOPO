from appium import webdriver
def init_driver():
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.0.0'
    desired_caps['deviceName'] = '192.168.27.101:5555'
    # app信息
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # server 启动参数

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver