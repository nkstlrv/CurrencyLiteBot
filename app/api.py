import requests
from datetime import datetime


iso_dict_decoder = {840: "usd", 980: "uah", 978: "eur"}


def get_hryvna_rate():
    response = requests.get("https://api.monobank.ua/bank/currency")

    if response.status_code == 200:
        try:
            data: list = response.json()[0:2]
        except IndexError or ValueError:
            return "Invalid response data"

        result = dict()
        for rate in data:
            result[iso_dict_decoder.get(rate.get("currencyCodeA"))] = {
                "buy": rate.get("rateBuy"),
                "sell": rate.get("rateSell"),
            }

        return result


if __name__ == "__main__":
    get_hryvna_rate()
