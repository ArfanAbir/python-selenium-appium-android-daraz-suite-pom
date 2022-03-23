import time

from Pages.BasePage import BasePage
from Pages.LaptopSearchPage import LaptopSearch


class DarazMobileAppTest(BasePage):

    def test_search_laptop(self):
        app = LaptopSearch(self.driver)
        app.click_first_next_button()
        app.change_language()
        app.skip_button_click()
        app.search_bar_icon()
        app.search_input_bar("laptop")
        app.click_search_btn()

