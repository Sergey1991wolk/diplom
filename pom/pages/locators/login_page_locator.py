from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


user_name_field = (By.ID, 'user_login')
user_password_field = (By.ID, 'user_pass')

wrong_login_message = (By.ID, 'login_error')

remember_me = (By.ID, 'rememberme')
login_button = (By.ID, 'wp-submit')
#visible_password = (By.XPATH("//button[@class='button button-secondary wp-hide-pw hide-if-no-js']"))


#lang_checkbox = (By.ID, 'language-switcher-locales')
#rem_me_check = (By.XPATH, '//div[@id="block_top_menu"]/ul/li[2]/a')
#lang_combobox = (By.CLASS_NAME, 'shopping_cart')
#lang_change_button = (By.CSS_SELECTOR, 'select[id="selectProductSort"]')
