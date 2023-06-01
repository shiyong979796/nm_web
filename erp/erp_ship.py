from common.basepage import Base_page
from selenium import webdriver
from selenium.webdriver.common.by import By
from erp.connect_server import run_erp2, run_erp
import requests
import time
from place_order import place_order
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

order_sn = place_order()
run_erp(order_sn)

url = 'http://erp.test.com:400/admin/privilege.php'
order_sn = order_sn

# 订单管理
loc_name = By.XPATH, '//input[@name="username"]'
loc_password = By.XPATH, '//input[@name="password"]'
loc_sign_in = By.XPATH, '//input[@type="submit"]'
# 客服管理菜单
loc_Customer = By.XPATH, '//span[@title="客服管理"]'
# 订单查询菜单
loc_Order_Management = By.XPATH, '//a[@title="客服订单查询"]'
iframe = By.ID, "main_frame"
search = By.XPATH, '//textarea[@class="form-control"]'
submit_order_sn = By.ID, 'checkStartTime'
order_detail = By.XPATH, '//td/a[@target="_blank"]'
loc_Confirm_Order = By.XPATH, '//a[contains(text(),"Confirm Order")]'
loc_submit_Confirm = By.XPATH, '//td/input[@value="Submit"]'
loc_erp_gd_sn = By.XPATH, '//a[@class="dispatchNum"]'

# 采购管理菜单
loc_purchase = By.XPATH, '//span[@title="采购管理"]'
# 工单管理菜单
loc_source_ = By.XPATH, '//a[@title="工单管理"]'
# 未制作的工单菜单
loc_Generate_Source_Order = By.XPATH, '//a[@title="未制作的工单"]'
loc_iframe2 = By.ID, 'main_frame'
loc_externalOrderSn = By.XPATH, '//input[@name="row[externalOrderSn]"]'
loc_select_option = By.XPATH, '//select[@name="or_email[]"]'
loc_yes_option = By.XPATH, '//select[@name="confirm_order"]/option[@value="Y"]'
loc_search_gd_button = By.XPATH, '//input[@value="查询待下工单 "]'
loc_create_gd_button = By.XPATH, '//a[contains(text(),"生成工单")]'
loc_create_gd_button2 = By.XPATH, '//input[@value=" 生成工单 "]'
loc_ship_time = By.XPATH, '//input[@id="shippingCalendar" ]'

loc_new_gd = By.XPATH, '//a[@title="未找到工厂的工单（新）"]'
loc_iframe3 = By.ID, 'main_frame'

loc_input_order = By.XPATH, '//input[@id="zzOrderSn"]'
loc_search_gd = By.XPATH, '//input[@value=" 查询工单 "]'
loc_select_operator = By.XPATH, '//td/select/option[text()="--选择供应商--"]//ancestor::select'
loc_allocation_gd = By.XPATH, '//input[@value="分派选择的工单"]'

loc_Warehouse = By.XPATH, '//span[text()="Warehouse"]'
loc_send_to_OW = By.XPATH, '//a[@title="发往海外"]'
loc_gd_rk = By.XPATH, '//a[contains(text(),"Entry Scan") and @title="工单入库" ]'
loc_multiBox = By.XPATH, '//input[@id="multiBox"]'
loc_singleBox = By.XPATH, '//input[@id="singleBox"]'
loc_gd_sn = By.XPATH, '//input[@id="dispatchListSn"]'
loc_kucun_box = By.XPATH, '//input[@id="kucunBox"]'
loc_submit_gd = By.XPATH, '//button[@id="singleBoxSubmit"]'
loc_kucunBoxButton = By.XPATH, '//button[@id="kucunBoxButton"]'
loc_singleBoxButton = By.XPATH, '//button[@id="singleBoxButton"]'
loc_multiBoxButton = By.XPATH, '//button[@id="multiBoxButton"]'

driver = webdriver.Chrome()
base = Base_page(driver)

driver.get(url)
driver.maximize_window()
for i in range(2):
    base.input_value(loc_name, 'test110')
    base.input_value(loc_password, '1234567')
    base.click_element(loc_sign_in)

base.click_element(loc_Customer)
base.click_element(loc_Order_Management)
driver.switch_to.frame(base.get_element(iframe))
base.input_value(search, order_sn)
base.click_element(submit_order_sn)
base.click_element(order_detail)
base.swich_to_window()
base.click_element(loc_Confirm_Order)
base.click_element(loc_submit_Confirm)
# 创建预定工单
run_erp2()
base.swich_to_window(old=True)
# 采购管理
base.click_element(loc_purchase)
# 工单管理
base.click_element(loc_source_)
base.click_element(loc_Generate_Source_Order)
driver.switch_to.frame(base.get_element(loc_iframe2))
base.input_value(loc_externalOrderSn, order_sn)
base.click_element(loc_select_option)
s1 = Select(base.get_element(loc_select_option))
s1.select_by_index(1)
base.click_element(loc_search_gd_button)
base.click_element(loc_create_gd_button)
base.click_element(loc_create_gd_button2)

# 回到主iframe
driver.switch_to.default_content()
# 分配工厂制作
base.click_element(loc_new_gd)
driver.switch_to.frame(base.get_element(loc_iframe3))
base.input_value(loc_input_order, order_sn)
# 查询工单
base.click_element(loc_search_gd)
# 点击选择供应商
base.click_element(loc_select_operator)
s2 = Select(base.get_element(loc_select_operator))
s2.select_by_index(1)
time.sleep(2)
base.click_element(loc_allocation_gd)
# 切换弹窗
base.swich_to_window()

driver.refresh()
# 获取erp工单号
erp_gd_sn = base.get_text(loc_erp_gd_sn)

# 切换弹窗
base.swich_to_window(True)
# 回到主frame
driver.switch_to.default_content()
# 点击Warehouse
base.click_element(loc_Warehouse)
time.sleep(1)
base.click_element(loc_send_to_OW)
base.click_element(loc_gd_rk)
time.sleep(5)
alert = driver.switch_to.alert  # 创建弹窗对象
alert.accept()  # 点击弹窗中的【确定】
driver.switch_to.frame(base.get_element(loc_iframe3))
base.input_value(loc_multiBox, 'bailu066', submit=True)
base.input_value(loc_singleBox, 'bailu065', submit=True)
#
# base.input_value(loc_kucun_box, 'KCbailu05', submit=True)
# base.input_value(loc_gd_sn, erp_gd_sn, submit=True)
# base.click_element(loc_submit_gd)
# time.sleep(5)
# try:
#     alert = driver.switch_to.alert  # 创建弹窗对象
#     alert.accept()  # 点击弹窗中的【确定】
# except:
#     pass
# base.click_element(loc_kucunBoxButton)
# base.click_element(loc_multiBoxButton)

if __name__ == '__main__':
    pass
