import requests
import time
from erp.connect_server import run_erp
import random

base_url = 'https://api-t-4.azazie.com'
head = {
    "Authorization": "",
    "x-app": "pc",
    "X-Token": "",
    "x-countryCode": "us",
    "x-languagecode": "en"
}


def login():
    url_login = '/1.0/user/login'
    login_data = {"email": "shiyong@gaoyaya.com",
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


def remove_card(rec_id, token):
    url_del_cart = f'/1.0/cart/goods/{rec_id}'
    head = {
        "Authorization": "",
        "x-app": "pc",
        "X-Token": token,
        "x-countryCode": "us",
        "x-languagecode": "en"
    }
    requests.delete(base_url + url_del_cart, headers=head)


def random_color_styleId(token, goods):
    head = {
        "Authorization": "",
        "x-app": "pc",
        "X-Token": token,
        "x-countryCode": "us",
        "x-languagecode": "en"
    }
    url = f'/1.0/product/first-screen?goods_id={goods}'
    res = requests.get(base_url + url, headers=head)
    color_dict = res.json()['data']['styleInfo']['color']
    li = []
    for k,v in color_dict.items():
        li.append(v['styleId'])

    styleId = random.choice(li)

    print(f'styleId :({styleId})')
    return styleId


def add_card(token, goods, styleId):
    url_add_card = '/1.0/cart/goods'
    head = {
        "Authorization": "",
        "x-app": "pc",
        "X-Token": token,
        "x-countryCode": "us",
        "x-languagecode": "en"
    }
    add_cart_data = {
        'goods_id': goods,
        'goods_number': 1,
        'dress_type': 'dress',
        'styles': {'select':
                       {'color': styleId, 'size': 7492}
                   }
    }
    res = requests.post(base_url + url_add_card, json=add_cart_data, headers=head)
    print(res.json()['data']['rec_id'])


def get_address_id(token):
    url_address = '/1.0/address/get'
    head = {
        "Authorization": "",
        "x-app": "pc",
        "X-Token": token,
        "x-countryCode": "us",
        "x-languagecode": "en"
    }
    res = requests.get(base_url + url_address, headers=head).json()
    address_id = res['data']['shippingAddress'][0]['addressId']
    return address_id


def create_order(token, address_id):
    url_create_order = '/1.0/order'
    head = {
        "Authorization": "",
        "x-app": "pc",
        "X-Token": token,
        "x-countryCode": "us",
        "x-languagecode": "en"
    }
    data = {"order_sn": "", "payment_id": 186, "shipping_method_id": 2, "address_id": address_id,
            "coupon_code": "forever111", "order_track_id": "", "event_date": "", "card_number": "6011111111111117",
            "exp_date": "12/2023", "month": "12", "year": "2023", "card_code": "022",
            "dot_list": "VersionA_GuestCheckout"}
    res = requests.post(base_url + url_create_order, json=data, headers=head)
    res_order = res.json()
    order_sn = res.json()['data']['orderSn']
    print(res_order)
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


def place_order():
    goods = '1009633'
    token = login()
    rec_id = cart_list(token)
    # if rec_id:
    remove_card(rec_id, token)
    color_id = random_color_styleId(token, goods)
    add_card(token, goods, color_id)
    address_id = get_address_id(token)
    order_sn = create_order(token, address_id)
    pyment(token, order_sn)
    return order_sn


if __name__ == '__main__':
    order_sn = place_order()
    run_erp(order_sn)
