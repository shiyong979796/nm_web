#:@ TIME 2022/1/2   10:27
#:@FILE  test_check_out.py
#:@EMAIL  1557225637@QQ.COM
import pytest
from page_object.list_page_bridsmaids import List_page_bridesmaids as BD
from page_object.home_page import Home_page


class Test_check_out:
    @pytest.mark.mark1
    @pytest.mark.usefixtures('init_fixture')
    def test_check_out_bd(self, init_fixture):
        Home_page(init_fixture).click_navigation_BD()
        BD(init_fixture).click_random_commodity()
