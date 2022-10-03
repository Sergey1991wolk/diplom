from selenium.webdriver.chrome.webdriver import WebDriver
from pom.pages.locators import profile_page_locator as loc


class ProfilePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get('https://dekarlab.de/wp/wp-admin/profile.php')

    def find_element(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)

    def find_elements(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)


    def light_color(self):
        return self.find_element(loc.light_color)

