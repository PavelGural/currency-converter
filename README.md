# Currency Converter

A simple command-line tool to convert USD, EUR, GBP, or RUB to Georgian Lari (GEL) using the official exchange rates from the National Bank of Georgia for a given date.

## Requirements
- Python 3.7+
- `requests` package

## Installation
1. (Optional) Create and activate a virtual environment:
   ```sh
   python3 -m venv myenv
   source myenv/bin/activate
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the script with the following command:

```sh
python main.py <CURRENCY> <DATE> <AMOUNT>
```

- `<CURRENCY>`: Currency code (USD, EUR, GBP, RUB)
- `<DATE>`: Date in `YYYY-MM-DD` format
- `<AMOUNT>`: Amount to convert (number)

### Example
Convert 100 USD to GEL on 2024-08-05:

```sh
python main.py USD 2024-08-05 100
```

## Output
The script will print the exchange rate and the converted amount in GEL.
