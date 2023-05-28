from common.basepage import Base_page
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'http://erp.test.com:400/admin/privilege.php'
order_sn = ''

loc_name = By.XPATH, '//input[@name="username"]'
loc_password = By.XPATH, '//input[@name="password"]'
loc_sign_in = By.XPATH, '//input[@type="submit"]'
loc_Customer = By.XPATH, '//span[@title="客服管理"]'
loc_Order_Management = By.XPATH, '//a[@title="客服订单查询"]'

iframe = By.ID, "main_frame"
search = By.XPATH, '//textarea[@class="form-control"]'
submit_order_sn = By.ID, 'checkStartTime'
order_detail = By.XPATH, '//td/a[@target="_blank"]'
a = By.XPATH, ''
a = By.XPATH, ''
a = By.XPATH, ''
a = By.XPATH, ''
a = By.XPATH, ''
a = By.XPATH, ''
a = By.XPATH, ''
a = By.XPATH, ''
a = By.XPATH, ''
a = By.XPATH, ''
a = By.XPATH, ''
a = By.XPATH, ''
a = By.XPATH, ''
a = By.XPATH, ''
a = By.XPATH, ''
a = By.XPATH, ''
a = By.XPATH, ''

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
