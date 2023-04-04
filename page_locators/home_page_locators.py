#:@ TIME 2021/12/20   16:08
#:@FILE  home_page_locators.py
#:@EMAIL  1557225637@QQ.COM
from selenium.webdriver.common.by import By


class Home_page_locators:
    home_user_email_text = By.ID, 'ht-login'

    navigations_BD = By.XPATH, '//a[@class="nav-a-link"]'
