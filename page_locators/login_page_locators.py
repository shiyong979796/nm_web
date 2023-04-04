#:@ TIME 2021/12/20   15:52
#:@FILE  login_page_locators.py
#:@EMAIL  1557225637@QQ.COM
from selenium.webdriver.common.by import By


# login页对象类
class Login_page_locators:
    # 用户名输入框
    input_email_elm = By.ID, '_email'
    # 密码输入框
    input_password_elm = By.ID, '_password'
    # 登录按钮
    login_button_elm = By.XPATH, '//button[@tabindex="4"]'

    # Please enter an email address.
    empty_user = By.XPATH, '//span[@class="waiting"]/following-sibling::span'
    # Please enter your password.
    empty_password = By.XPATH, '//input[@id="_password"]/following::span'
    # Please enter a valid email.
    invalid_email = By.XPATH, '//span[@class="waiting"]/following-sibling::span'
    # The email address or password you entered is incorrect.
    password_error = By.XPATH, '//span[@class="help-block"]'
