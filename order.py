# Реализовать методы для выставления ордера на покупку/продажу у класса CryptoBot
import requests


class CryptoBot:

    def __init__(self, url, public_key, secret):
        self.url = url + "/api/2"
        self.session = requests.session()
        self.session.auth = (public_key, secret)


    def newOrder(self, client_order_id, symbol_code, side, quantity, price):
        """
        параметры:
        : client_order_id - Уникальный идентификатор для заказа, назначенный трейдером
        : symbol_code - Торговый символ - пара валют (например, "ETHBTC")
        : side - ордер на продажу или покупку - shell/buy
        : quantity - количество желаемых сделок
        : price - стоимость сделки (только для limit)

        """

        order = {'symbol': symbol_code,
                 'side': side,
                 'quantity': quantity,
                 'price': price}

        return self.session.put("%s/order/%s" % (self.url, client_order_id), order=order).json()




if __name__ == 'main':
    pass

