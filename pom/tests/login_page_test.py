import conftest
from pom.pages.login_page import LoginPage
from selenium.webdriver.support.ui import Select


def test_sc_submit_rem_me_not_set(driver):
    login_page = LoginPage(driver)
    login_page.open()
    user_name_field = login_page.user_name_field()
    user_name_field.click()
    user_name_field.send_keys('wf.anna@gmail.com')
    password_field = login_page.user_password_field()
    password_field.click()
    password_field.send_keys('1Vk9rU&i@NtvD3pVf70y5UEu')
    login_page.login_button().submit()
    driver.close()
    driver_new = conftest.init_driver()
    login_page_new = LoginPage(driver_new)
    login_page_new.open()
    assert login_page_new.user_name_field() is not None

def test_sc_submit_rem_me_set(driver):
    login_page = LoginPage(driver)
    login_page.open()
    user_name_field = login_page.user_name_field()
    user_name_field.click()
    user_name_field.send_keys('wf.anna@gmail.com')
    password_field = login_page.user_password_field()
    password_field.click()
    password_field.send_keys('1Vk9rU&i@NtvD3pVf70y5UEu')
    remember_me = login_page.remember_me_field()
    remember_me.click()
    login_page.login_button().submit()
    cookies = driver.get_cookies()
    driver.close()
    driver_new = conftest.init_driver()
    driver_new.get('https://dekarlab.de')
    for cookie in cookies:
        driver_new.add_cookie(cookie)
    login_page_new = LoginPage(driver_new)
    login_page_new.open()
    is_user_name_exists = True
    try:
        login_page_new.user_name_field()
    except:
        print("User_name is not on the page.")
        is_user_name_exists = False
    assert is_user_name_exists == False

def test_sc_wrong_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    user_name_field = login_page.user_name_field()
    user_name_field.click()
    user_name_field.send_keys('wf.anna@gmail.com')
    password_field = login_page.user_password_field()
    password_field.click()
    password_field.send_keys('1Vk9rU&i@NtvD3pVf78y5UEu')
    login_page.login_button().submit()
    assert login_page.wrong_login_message().text == 'Error: the password you entered for the email address ' \
                                                    'wf.anna@gmail.com is incorrect. Lost your password?'

def test_sc_lang_combobox(driver):
    login_page = LoginPage(driver)
    login_page.open()
    lang_combobox = login_page.lang_combobox()
    lang_combobox.click()
    Select(lang_combobox).select_by_value('de_DE')
    lang_combobox.click()
    assert Select(lang_combobox).all_selected_options[0].text == 'Deutsch'

def test_sc_lang_combobox_en_US(driver):
    login_page = LoginPage(driver)
    login_page.open()
    lang_combobox = login_page.lang_combobox()
    lang_combobox.click()
    Select(lang_combobox).select_by_value('en_US')
    lang_combobox.click()
    assert Select(lang_combobox).all_selected_options[0].text == 'English (United States)'

def test_sc_lang_combobox_en_GB(driver):
    login_page = LoginPage(driver)
    login_page.open()
    lang_combobox = login_page.lang_combobox()
    lang_combobox.click()
    Select(lang_combobox).select_by_value('en_GB')
    lang_combobox.click()
    assert Select(lang_combobox).all_selected_options[0].text == 'English (UK)'
