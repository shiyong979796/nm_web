#:@ TIME 2021/12/20   13:01
#:@FILE  home_page.py
#:@EMAIL  1557225637@QQ.COM
import time

from selenium.webdriver.remote.webdriver import WebDriver
from page_locators.home_page_locators import Home_page_locators as Home
from common.basepage import Base_page


class Home_page(Base_page):

    # 登录成功 预期方法
    def expect_login_succeed(self):
        time.sleep(2)
        user_tetx = self.get_text(Home.home_user_email_text, '获取登录后的email')
        return user_tetx

    def click_navigation_BD(self):
        self.click_element(Home.navigations_BD, '点击 导航栏 BRIDESMAIDS', 1)
