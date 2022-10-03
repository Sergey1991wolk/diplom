from pom.pages.login_page import LoginPage


class TestUtil:
    def login(driver):
        login_page = LoginPage(driver)
        login_page.open()
        user_name_field = login_page.user_name_field()  #логинимся ввод пороля без remember me,
        user_name_field.click()
        user_name_field.send_keys('wf.anna@gmail.com')
        password_field = login_page.user_password_field()
        password_field.click()
        password_field.send_keys('1Vk9rU&i@NtvD3pVf70y5UEu')
        remember_me = login_page.remember_me_field()
        remember_me.click()
        login_page.login_button().submit()