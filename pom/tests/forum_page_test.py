from selenium.webdriver import Keys
from pom.pages.forum_page import ForumPage
from pom.pages.login_page import LoginPage
from pom.tests.test_until import TestUtil
from time import sleep


def test_sc_find_forum(driver):
    login_page = LoginPage(driver)
    login_page.open()
    user_name_field = login_page.user_name_field()
    user_name_field.click()
    user_name_field.send_keys('wf.anna@gmail.com')
    password_field = login_page.user_password_field()
    password_field.click()
    password_field.send_keys('1Vk9rU&i@NtvD3pVf70y5UEu')
    login_page.login_button().submit()
    forum_page = ForumPage(driver)
    forum_page.open()
    is_forum_exists = True
    try:
        forum_page.private_project()
    except:
        print("Forum is not on the page.")
        is_forum_exists = False
    assert is_forum_exists == True

def test_sc_forum_without_login(driver):
    forum_page = ForumPage(driver)
    forum_page.open()
    is_forum_exists = True
    try:
        forum_page.private_project()
    except:
        print("Forum is not on the page.")
        is_forum_exists = False
    assert is_forum_exists == False

def test_sc_forum_without_login_error_message(driver):
    forum_page = ForumPage(driver)
    forum_page.open()
    assert forum_page.forum_without_login_error_message().text == 'Oh, bother! No forums were found here.'

def test_find_forum(driver):
    TestUtil.login(driver)
    forum_page = ForumPage(driver)
    forum_page.open()
    find_forum = forum_page.find_forum()
    find_forum.click()
    find_forum.send_keys('money')
    find_forum.send_keys(Keys.ENTER)
    find_results = forum_page.find_results()
    assert find_results.text == 'SEARCH RESULTS FOR: MONEY'

def test_nothing_find_forum(driver):
    TestUtil.login(driver)
    forum_page = ForumPage(driver)
    forum_page.open()
    find_forum = forum_page.find_forum()
    find_forum.click()
    find_forum.send_keys('Go to first line in file')
    find_forum.send_keys(Keys.ENTER)
    find_nothing_results = forum_page.find_nothing_results()
    assert find_nothing_results.text == 'Nothing Found'
    sleep(5)
