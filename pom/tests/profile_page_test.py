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
    modern = profile_page.modern_color()
    modern.click()
    assert modern.accessible_name == 'Modern'


 #   def test_sc_color_profile_evergreen
  #      def test_sc_color_profile_mint
   #         def test_sc_color_profile_blue
# def test_sc_color_profile_coffee
#def test_sc_color_profile_ectoplasm
#def test_sc_color_profile_mindnight
#def test_sc_color_profile_ocean
#def test_sc_color_profile_sunrise


def test_nickname(driver):
    TestUtil.login(driver)
    profile_page = ProfilePage(driver)
    profile_page.open()
    nickname = profile_page.nickname()
    assert nickname.get_attribute('value') == 'user'



