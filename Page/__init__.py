from selenium.webdriver.common.by import By

"""
配网页面定位信息
"""
# SmartLink配网
smartLinkBtn = (By.XPATH,"//*[contains(@text,'8.先(组播+广播)后Ap')]")
# 输入密码
smartLinkPwd = (By.ID,"com.het.bind.telecom:id/pass")
# 配网按钮
confirmBtn = (By.ID,"com.het.bind.telecom:id/bind_next")
