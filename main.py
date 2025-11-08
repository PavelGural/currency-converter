# python main.py USD 2024-08-05 100
import argparse
import json
import logging
from datetime import datetime
from decimal import Decimal
import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

NBG_API_URL = "https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/en/json/?date={date}"

def fetch_exchange_rates(date):
    url = NBG_API_URL.format(date=date)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def find_currency_rate(data, currency_code):
    currencies = data[0]['currencies']
    for currency in currencies:
        if currency['code'] == currency_code:
            return Decimal(currency['rate']) / Decimal(currency['quantity'])
    raise ValueError(
        f"Currency {currency_code} not found in the exchange rates data.")


def convert_to_lari(amount, rate):
    return amount * rate


def main():
    parser = argparse.ArgumentParser(
        description="Convert currency to Georgian Lari")
    parser.add_argument("currency", choices=[
                        "USD", "EUR", "GBP", "RUB"], help="Currency code")
    parser.add_argument("date", type=lambda s: datetime.strptime(
        s, '%Y-%m-%d').date(), help="Date in YYYY-MM-DD format")
    parser.add_argument("amount", type=Decimal, help="Amount to convert")

    args = parser.parse_args()

    try:
        exchange_rates = fetch_exchange_rates(args.date)
        rate = find_currency_rate(exchange_rates, args.currency)
        result = convert_to_lari(args.amount, rate)

        logger.info(
            f"Date: {args.date}, Currency: {args.currency}, Rate: {rate:.4f}, Amount: {args.amount}, Result in Lari: {result:.2f}")
        logger.info(
            f"{args.amount} {args.currency} (1 {args.currency} = {rate:.4f} GEL) is equal to {result:.2f} GEL on {args.date}")
    except requests.RequestException as e:
        logger.error(f"Error fetching exchange rates: {e}")
    except ValueError as e:
        logger.error(f"Error: {e}")
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
