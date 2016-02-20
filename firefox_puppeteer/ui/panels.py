
from firefox_puppeteer.ui_base_lib import UIBaseLib


class BasePanel(UIBaseLib):

    def __eq__(self, other):
        return self.element.get_attribute('id') == other.element.get_attribute('id')

    def __ne__(self, other):
        return self.element.get_attribute('id') != other.element.get_attribute('id')

    def __str__(self):
        return self.element.get_attribute('id')
