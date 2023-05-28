from common.basepage import Base_page
from selenium import webdriver
from selenium.webdriver.common.by import By
from erp.connect_server import run_erp2, run_erp
import requests
import time

base_url = 'https://api-t-4.azazie.com'
head = {
    "Authorization": "",
    "x-app": "pc",
    "X-Token": "",
    "x-countryCode": "us",
    "x-languagecode": "en"
}


def place_order():
    ulr_get_address = '/1.0/address/get'


def ship():
    url = 'http://erp.test.com:400/admin/privilege.php'
    order_sn = 'ZZ7151603960'
    order_sn = 'ZZ7151603960'

    loc_name = By.XPATH, '//input[@name="username"]'
    loc_password = By.XPATH, '//input[@name="password"]'
    loc_sign_in = By.XPATH, '//input[@type="submit"]'
    loc_Customer = By.XPATH, '//span[@title="客服管理"]'
    loc_Order_Management = By.XPATH, '//a[@title="客服订单查询"]'

    iframe = By.ID, "main_frame"
    search = By.XPATH, '//textarea[@class="form-control"]'
    submit_order_sn = By.ID, 'checkStartTime'
    order_detail = By.XPATH, '//td/a[@target="_blank"]'
    loc_Confirm_Order = By.XPATH, '//a[contains(text(),"Confirm Order")]'
    loc_submit_Confirm = By.XPATH, '//td/input[@value="Submit"]'
    loc_purchase = By.XPATH, '//span[@title="采购管理"]'
    loc_source_ = By.XPATH, 'title="工单管理"'
    loc_Generate_Source_Order = By.XPATH, '//a[@title="未制作的工单"]'
    loc_externalOrderSn = By.XPATH, '//input[@name="row[externalOrderSn]"]'
    loc_select_option = By.XPATH, '//select[@name="or_email[]"]'
    loc_yes_option = By.XPATH, '//select[@name="confirm_order"]/option[@value="Y"]'
    loc_search_gd_button = By.XPATH, '//input[@value="查询待下工单 "]'
    loc_create_gd_button = By.XPATH, '//a[contains(text(),"生成工单")]'
    loc_create_gd_button2 = By.XPATH, '//input[@value=" 生成工单 "]'
    loc_ship_time = By.XPATH, '//input[@id="shippingCalendar" ]'
    loc_ = By.XPATH, ''
    loc_ = By.XPATH, ''
    loc_ = By.XPATH, ''
    loc_ = By.XPATH, ''
    loc_ = By.XPATH, ''
    loc_ = By.XPATH, ''
    loc_ = By.XPATH, ''
    loc_ = By.XPATH, ''
    loc_ = By.XPATH, ''
    loc_ = By.XPATH, ''
    loc_ = By.XPATH, ''
    loc_ = By.XPATH, ''
    loc_ = By.XPATH, ''
    loc_ = By.XPATH, ''
    loc_ = By.XPATH, ''

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
    try:
        base.click_element(order_detail)
    except:
        run_erp(order_sn)
        base.click_element(submit_order_sn)
        base.click_element(order_detail)
    base.swich_to_window()
    base.click_element(loc_Confirm_Order)
    base.click_element(loc_submit_Confirm)
    # 创建预定工单
    run_erp2()
    base.click_element(loc_purchase)
    base.click_element(loc_source_)
    base.click_element(loc_Generate_Source_Order)
    base.input_value(loc_externalOrderSn, order_sn)
    base.click_element(loc_select_option)
    base.click_element(loc_yes_option)
    base.click_element(loc_search_gd_button)
    base.click_element(loc_create_gd_button)
    base.click_element(loc_create_gd_button2)


def login():
    url_login = '/1.0/user/login'
    login_data = {"email": "test_shiyongdt1@gaoyaya.com",
                  "password": "123456"}
    res = requests.post(url=base_url + url_login, json=login_data, headers=head)
    token = res.json()['data']['token']
    return token


def cart_list(token):
    url_cart_list = '/1.0/cart'
    new_heads = {
        "Authorization": "",
        "x-app": "pc",
        "X-Token": token,
        "x-countryCode": "us",
        "x-languagecode": "en"
    }
    res = requests.get(base_url + url_cart_list, headers=new_heads)
    checkoutGoodsList = res.json()['data']['checkoutGoodsList']
    if checkoutGoodsList:
        rec_id = checkoutGoodsList[0]['recId']
        print(rec_id)
        return rec_id
    else:
        return None


def remove_card(rec_id):
    url_del_cart = f'/1.0/cart/goods/{rec_id}'
    head = {
        "Authorization": "",
        "x-app": "pc",
        "X-Token": token,
        "x-countryCode": "us",
        "x-languagecode": "en"
    }
    requests.delete(base_url + url_del_cart, headers=head)


def add_card(token):
    url_add_card = '/1.0/cart/goods'
    head = {
        "Authorization": "",
        "x-app": "pc",
        "X-Token": token,
        "x-countryCode": "us",
        "x-languagecode": "en"
    }
    add_cart_data = {
        'goods_id': 1051099,
        'goods_number': 1,
        'dress_type': 'dress',
        'styles': {'select':
                       {'color': 531, 'size': 7493}
                   }
    }
    res = requests.post(base_url + url_add_card, json=add_cart_data, headers=head)
    print(res.json()['data']['rec_id'])


def create_order(token):
    url_create_order = '/1.0/order'
    head = {
        "Authorization": "",
        "x-app": "pc",
        "X-Token": token,
        "x-countryCode": "us",
        "x-languagecode": "en"
    }
    data = {"order_sn": "", "payment_id": 186, "shipping_method_id": 2, "address_id": 3584737,
            "coupon_code": "forever111", "order_track_id": "", "event_date": "", "card_number": "6011111111111117",
            "exp_date": "12/2023", "month": "12", "year": "2023", "card_code": "022",
            "dot_list": "VersionA_GuestCheckout"}
    res = requests.post(base_url + url_create_order, json=data, headers=head)
    order_sn = res.json()['data']['orderSn']
    print(order_sn)
    return order_sn


def pyment(token, order_sn):
    url_pyment = '/1.0/order/payment'
    head = {
        "Authorization": "",
        "x-app": "pc",
        "X-Token": token,
        "x-countryCode": "us",
        "x-languagecode": "en"
    }
    data = {"nonce": "", "order_sn": order_sn, "REF": "10111010", "device_id": 200761740,
            "use_account_balance": False}
    res = requests.post(base_url + url_pyment, json=data, headers=head)
    print('支付成功')


token = login()

rec_id = cart_list(token)
if rec_id:
    remove_card(rec_id)

add_card(token)

order_sn = create_order(token)

pyment(token, order_sn)
