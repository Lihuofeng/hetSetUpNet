from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Remote()

    def myFindElement(self, loc, timeout=10, poll=0.5):
        """
        :param loc:元组 例如（By.ID,ID属性自)
        :param timeout
        :param poll
        :return:返回定位对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def myFindElements(self, loc, timeout=10, poll=0.5):
        """
        :param loc:元组 例如（By.ID,ID属性自)
        :param timeout
        :param poll
        :return:返回定位对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def clickElement(self,loc):
        # 点击元素
        self.myFindElement(loc).click()
    def inputText(self,loc,text):
        input = self.myFindElement(loc)
        input.clear()
        input.send_keys(text)
