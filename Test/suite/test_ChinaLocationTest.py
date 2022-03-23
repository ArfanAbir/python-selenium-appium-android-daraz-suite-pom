import time

from Pages.BasePage import BasePage
from Pages.ChinaPage import ChinaLocation


class DarazMobileAppTest(BasePage):

    def test_chinalocation(self):
        app = ChinaLocation(self.driver)
        app.click_first_next_button()
        app.change_language()
        app.skip_button_click()
        app.search_bar_icon()
        app.search_input_bar("laptop")
        app.click_search_btn()
        app.filter_icon()
        app.china_location()
        app.done_btn()

