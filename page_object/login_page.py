#:@ TIME 2021/12/19   23:38
#:@FILE  login_page.py
#:@EMAIL  1557225637@QQ.COM

from common.basepage import Base_page
from page_locators.login_page_locators import Login_page_locators as lg


# login页 功能调用类
class Login_page(Base_page):

    # 登录成功功能
    def login(self, email, password):
        # login
        self.input_value(lg.input_email_elm, '输入email', email)
        self.input_value(lg.input_password_elm, '输入密码', password)
        self.click_element(lg.login_button_elm, '点击登录')

    # def get_all_data_empty_msg(self):
    #     return self.get_text(lg.empty_user,'全部参数为空')
    #
    # def get_emial_empty(self):
    #     return self.get_text(lg.empty_user,'用户名为空')
    #
    # def get_password_empty(self):
    #     return self.get_text(lg.empty_password,'为空的密码')
    #
    # def get_invalid_email(self):
    #     return self.get_text(lg.invalid_email,'无效的email')
    # def
