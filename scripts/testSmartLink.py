import sys, os

sys.path.append(os.getcwd())
from Base.InitDriver import init_driver
from Page.PageObj import PageObj
import pytest


class TestSmartLink:
    def setup_class(self):
        # 实例化driver
        self.driver = init_driver()
        self.po = PageObj(self.driver).reSmartLinkPage()

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope="class")
    def clickSmartLink(self):
        self.po.clickSmartLinkBtn()

    @pytest.mark.usefixtures("clickSmartLink")
    @pytest.mark.parametrize("pwd", ["123451234512345"])
    def testSmartLink(self, pwd):
        self.po.pwdInput(pwd)
