from selenium.webdriver.support.select import Select
from pom.pages.profile_page import ProfilePage
from pom.tests.test_until import TestUtil


def test_sc_color_profile_light(driver):
    TestUtil.login(driver)
    profile_page = ProfilePage(driver)
    profile_page.open()
    light_color = profile_page.light_color()
    light_color.click()
    assert light_color.accessible_name == 'Light'

def test_sc_color_profile_modern(driver):
    TestUtil.login(driver)
    profile_page = ProfilePage(driver)
    profile_page.open()
    modern_color = profile_page.modern_color()
    modern_color.click()
    assert modern_color.accessible_name == 'Modern'

def test_sc_color_profile_evergreen(driver):
    TestUtil.login(driver)
    profile_page = ProfilePage(driver)
    profile_page.open()
    evergreen_color = profile_page.evergreen_color()
    evergreen_color.click()
    assert evergreen_color.accessible_name == 'Evergreen'

def test_sc_color_profile_mint(driver):
    TestUtil.login(driver)
    profile_page = ProfilePage(driver)
    profile_page.open()
    mint_color = profile_page.mint_color()
    mint_color.click()
    assert mint_color.accessible_name == 'Mint'

def test_sc_color_profile_blue(driver):
    TestUtil.login(driver)
    profile_page = ProfilePage(driver)
    profile_page.open()
    blue_color = profile_page.blue_color()
    blue_color.click()
    assert blue_color.accessible_name == 'Blue'

def test_sc_color_profile_coffee(driver):
    TestUtil.login(driver)
    profile_page = ProfilePage(driver)
    profile_page.open()
    coffee_color = profile_page.coffee_color()
    coffee_color.click()
    assert coffee_color.accessible_name == 'Coffee'

def test_sc_color_profile_ectoplasm(driver):
    TestUtil.login(driver)
    profile_page = ProfilePage(driver)
    profile_page.open()
    ectoplasm_color = profile_page.ectoplasm_color()
    ectoplasm_color.click()
    assert ectoplasm_color.accessible_name == 'Ectoplasm'

def test_sc_color_profile_midnight(driver):
    TestUtil.login(driver)
    profile_page = ProfilePage(driver)
    profile_page.open()
    midnight_color = profile_page.midnight_color()
    midnight_color.click()
    assert midnight_color.accessible_name == 'Midnight'

def test_sc_color_profile_ocean(driver):
    TestUtil.login(driver)
    profile_page = ProfilePage(driver)
    profile_page.open()
    ocean_color = profile_page.ocean_color()
    ocean_color.click()
    assert ocean_color.accessible_name == 'Ocean'

def test_sc_color_profile_sunrise(driver):
    TestUtil.login(driver)
    profile_page = ProfilePage(driver)
    profile_page.open()
    sunrise_color = profile_page.sunrise_color()
    sunrise_color.click()
    assert sunrise_color.accessible_name == 'Sunrise'

def test_nickname(driver):
    TestUtil.login(driver)
    profile_page = ProfilePage(driver)
    profile_page.open()
    nickname = profile_page.nickname()
    assert nickname.get_attribute('value') == 'user'

def test_first_name(driver):
    TestUtil.login(driver)
    profile_page = ProfilePage(driver)
    profile_page.open()
    first_name = profile_page.first_name()
    assert first_name.get_attribute('value') == '123'

def test_last_name(driver):
    TestUtil.login(driver)
    profile_page = ProfilePage(driver)
    profile_page.open()
    last_name = profile_page.last_name()
    assert last_name.get_attribute('value') == '345'

def test_email(driver):
    TestUtil.login(driver)
    profile_page = ProfilePage(driver)
    profile_page.open()
    email_name = profile_page.email_name()
    assert email_name.get_attribute('value') == 'wf.anna@gmail.com'

def test_website(driver):
    TestUtil.login(driver)
    profile_page = ProfilePage(driver)
    profile_page.open()
    website_profile = profile_page.website_profile()
    assert website_profile .get_attribute('value') == 'http://bla'

def test_description(driver):
    TestUtil.login(driver)
    profile_page = ProfilePage(driver)
    profile_page.open()
    biographical_info = profile_page.website_profile()
    biographical_info.click()
    biographical_info.send_keys('user biographical')

def test_new_application_password_name(driver):
    TestUtil.login(driver)
    profile_page = ProfilePage(driver)
    profile_page.open()
    new_password_name = profile_page.new_password_name()
    new_password_name.click()
    new_password_name.send_keys('7867292')
    do_new_password = profile_page.do_new_password()
    do_new_password.click()
    update_profile = profile_page.update_profile()
    update_profile.click()

def test_sc_lang_combobox(driver):
    TestUtil.login(driver)
    profile_page = ProfilePage(driver)
    profile_page.open()
    lang_combobox = profile_page.lang_combobox()
    lang_combobox.click()
    Select(lang_combobox).select_by_value('de_DE')
    lang_combobox.click()
    assert Select(lang_combobox).all_selected_options[0].text == 'Deutsch'

def test_sc_lang_combobox_en_US(driver):
    TestUtil.login(driver)
    profile_page = ProfilePage(driver)
    profile_page.open()
    lang_combobox = profile_page.lang_combobox()
    lang_combobox.click()
    Select(lang_combobox).select_by_value('')
    lang_combobox.click()
    assert Select(lang_combobox).all_selected_options[0].text == 'English (United States)'

def test_sc_lang_combobox_en_GB(driver):
    TestUtil.login(driver)
    profile_page = ProfilePage(driver)
    profile_page.open()
    lang_combobox = profile_page.lang_combobox()
    lang_combobox.click()
    Select(lang_combobox).select_by_value('en_GB')
    lang_combobox.click()
    assert Select(lang_combobox).all_selected_options[0].text == 'English (UK)'
