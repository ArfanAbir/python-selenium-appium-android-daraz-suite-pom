import time

from Pages.BasePage import BasePage
from Pages.HPPage import HpLaptop


class DarazMobileAppTest(BasePage):

    def test_hp_laptop(self):
        app = HpLaptop(self.driver)
        app.click_first_next_button()
        app.change_language()
        app.skip_button_click()
        app.search_bar_icon()
        app.search_input_bar("laptop")
        app.click_search_btn()
        app.filter_icon()
        app.hp_laptop()
        app.done_btn()

