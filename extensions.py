import json
import requests
from config import keys

class ConvertionException(Exception):
    pass

class APIException:
    @staticmethod
    def get_price(quote:str, base:str, amount:str):
        quote_ticker = keys[quote]
        base_ticker = keys[base]

        if quote == base:
            raise ConvertionException(f"Невозможно перевести одинаковые валюты {base}.")
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {quote}.")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {base}.")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Не удалось обработать количество {amount}.")

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        total_base = round(json.loads(r.content)[keys[base]]*amount)
        return total_base