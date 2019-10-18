from Page.SmartLinkPage import SmartLinkPage
class PageObj:
    def __init__(self,driver):
        self.driver =driver
    def reSmartLinkPage(self):
        # 返回搜索页面
        return SmartLinkPage(self.driver)