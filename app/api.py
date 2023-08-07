import requests
from dotenv import load_dotenv
import os
import freecurrencyapi

load_dotenv()
CURRENCY_API_KEY = os.getenv("FREECURRENCY_API_KEY")

# client to handle freecurrencyapi API through library instead of direct requests
client = freecurrencyapi.Client(CURRENCY_API_KEY)

iso_dict_decoder = {840: "usd", 980: "uah", 978: "eur"}


def get_hryvna_rate():
    response = requests.get(
        "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11"
    )
    if response.status_code == 200:
        try:
            data: list = response.json()

            result = dict()

            for currency in data:
                result[currency.get("ccy")] = currency
                currency.pop("ccy")

            return result
        except (
            IndexError or ValueError
        ):  # It means that api server returned invalid data
            return None


def calculate_currency_rate(
    currency_to_sell: str, currency_to_buy: str, amount: float | int
):
    if "UAH" not in (currency_to_buy, currency_to_sell):
        try:
            currency_rate = client.latest(base_currency=currency_to_sell)["data"].get(
                currency_to_buy
            )
            if currency_rate:
                result = currency_rate * amount
                return round(result, 3)
        except Exception as ex:
            return None
    else:
        uah_rate = get_hryvna_rate()
        if uah_rate:
            if currency_to_sell == currency_to_buy:
                return amount

            elif currency_to_sell == "UAH":
                exchange_currency_data = uah_rate.get(currency_to_buy)
                if exchange_currency_data:
                    result = exchange_currency_data.get("sale")
                    return result

            elif currency_to_buy == "UAH":
                exchange_currency_data = uah_rate.get(currency_to_sell)
                if exchange_currency_data:
                    result = exchange_currency_data.get("buy")
                    return result


if __name__ == "__main__":
    # print(get_hryvna_rate())
    print(calculate_currency_rate("UAH", "UAH", 1))
