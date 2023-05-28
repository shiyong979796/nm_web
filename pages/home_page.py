#:@ TIME 2021/12/20   16:08
#:@FILE  home_page.py
#:@EMAIL  1557225637@QQ.COM
from selenium.webdriver.common.by import By
import time
from common.basepage import Base_page


class HomePage(Base_page):
    home_user_email_text = By.ID, 'ht-login'

    navigations_BD = By.XPATH, '//a[@class="nav-a-link"]'

    # 登录成功 预期方法
    def expect_login_succeed(self):
        time.sleep(2)
        user_tetx = self.get_text(self.home_user_email_text, '获取登录后的email')

        return user_tetx

    def click_navgation_BD(self):
        self.click_element(self.navigations_BD, '点击 导航栏 BRIDESMAIDS', 1)
