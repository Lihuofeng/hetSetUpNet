from Base.Base import Base
import Page


class SmartLinkPage(Base):
    def __init__(self, driver):
        # 初始化父类
        Base.__init__(self, driver)

    def clickSmartLinkBtn(self):
        # 点击SmartLink按钮
        self.clickElement(Page.smartLinkBtn)

    def pwdInput(self, pwd):
        # 输入密码
        self.inputText(Page.smartLinkPwd, pwd)

    def confirmBtn(self):
        self.clickElement(Page.confirmBtn)
