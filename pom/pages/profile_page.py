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

    def modern_color(self):
        return self.find_element(loc.modern_color)

    def evergreen_color(self):
        return self.find_element(loc.evergreen_color)

    def mint_color(self):
        return self.find_element(loc.mint_color)

    def blue_color(self):
        return self.find_element(loc.blue_color)

    def coffee_color(self):
        return self.find_element(loc.coffee_color)

    def ectoplasm_color(self):
        return self.find_element(loc.ectoplasm_color)

    def midnight_color(self):
        return self.find_element(loc.midnight_color)

    def ocean_color(self):
        return self.find_element(loc.ocean_color)

    def sunrise_color(self):
        return self.find_element(loc.sunrise_color)

    def nickname(self):
        return self.find_element(loc.nickname)

    def first_name(self):
        return self.find_element(loc.first_name)

    def last_name(self):
        return self.find_element(loc.last_name)

    def email_name(self):
        return self.find_element(loc.email_name)

    def website_profile(self):
        return self.find_element(loc.website_profile)

    def biographical_info(self):
        return self.find_element(loc.biographical_info)

    def new_password_name(self):
        return self.find_element(loc.new_password_name)

    def do_new_password(self):
        return self.find_element(loc.do_new_password)

    def update_profile(self):
        return self.find_element(loc.update_profile)
