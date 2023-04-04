#:@ TIME 2022/1/2   10:14
#:@FILE  list_page_bridsmaids.py
#:@EMAIL  1557225637@QQ.COM
from page_locators.list_page_bridesmaids_locators import List_page_bridesmaids_locators as BD
from common.basepage import Base_page
import random


class List_page_bridesmaids(Base_page):

    def click_random_commodity(self):
        rd = random.randint(0, 60)
        # loc_obj=self.get_element(BD.all_commoditys,'随机 点击BD列表页商品',rd)

        self.click_element(BD.all_commoditys, '随机 点击BD列表页商品', rd)
