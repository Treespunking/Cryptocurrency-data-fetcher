import requests
import os
import csv
import logging
import time
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),      # Log to a file
        logging.StreamHandler()             # Also log to console
    ]
)

# Load environment variables from .env file
try:
    load_dotenv()
except Exception as e:
    logging.error(f"Failed to load .env file: {e}")
    exit(1)

# Load coin IDs from output_ids.txt
coin_ids_file = 'output_ids.txt'

try:
    if not os.path.exists(coin_ids_file):
        logging.error(f"File {coin_ids_file} not found.")
        exit(1)

    with open(coin_ids_file, 'r') as f:
        coin_ids = [line.strip() for line in f if line.strip()]

    if not coin_ids:
        logging.error("No coin IDs found in the file.")
        exit(1)

except Exception as e:
    logging.error(f"Error reading coin IDs: {e}")
    exit(1)

# Get API key from environment
api_key = os.getenv("COINGECKO_API_KEY")
if not api_key:
    logging.error("API key not found in .env file.")
    exit(1)

# API Setup - FIXED: Removed the extra space after "markets"
url_base = "https://api.coingecko.com/api/v3/coins/markets"
headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": api_key
}
params_base = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'sparkline': False,
    'per_page': 100,
    'page': 1
}

# Batched requests
batch_size = 200
all_data = []

for i in range(0, len(coin_ids), batch_size):
    batch = coin_ids[i:i + batch_size]
    params = params_base.copy()
    params['ids'] = ','.join(batch)

    try:
        logging.info(f"Fetching batch {i // batch_size + 1}: {len(batch)} coins")
        response = requests.get(url_base, headers=headers, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors

        batch_data = response.json()
        if batch_data:
            all_data.extend(batch_data)
        else:
            logging.warning(f"Empty response for batch starting at {i}")

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed for batch starting at {i}: {e}")
        exit(1)

    time.sleep(2)  # Rate limiting safety

# Output to CSV
csv_file = 'crypto_data.csv'

try:
    if not all_data:
        logging.error("No data returned from the API.")
        exit(1)

    # Define fieldnames based on expected structure
    fieldnames = [
        "id", "symbol", "name", "current_price", "market_cap", "market_cap_rank",
        "fully_diluted_valuation", "total_volume", "high_24h", "low_24h",
        "price_change_24h", "price_change_percentage_24h", "market_cap_change_24h",
        "market_cap_change_percentage_24h", "circulating_supply", "total_supply",
        "max_supply", "ath", "ath_change_percentage", "ath_date", "atl",
        "atl_change_percentage", "atl_date", "last_updated"
    ]

    with open(csv_file, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for coin in all_data:
            writer.writerow({
                'id': coin.get('id'),
                'symbol': coin.get('symbol'),
                'name': coin.get('name'),
                'current_price': coin.get('current_price'),
                'market_cap': coin.get('market_cap'),
                'market_cap_rank': coin.get('market_cap_rank'),
                'fully_diluted_valuation': coin.get('fully_diluted_valuation'),
                'total_volume': coin.get('total_volume'),
                'high_24h': coin.get('high_24h'),
                'low_24h': coin.get('low_24h'),
                'price_change_24h': coin.get('price_change_24h'),
                'price_change_percentage_24h': coin.get('price_change_percentage_24h'),
                'market_cap_change_24h': coin.get('market_cap_change_24h'),
                'market_cap_change_percentage_24h': coin.get('market_cap_change_percentage_24h'),
                'circulating_supply': coin.get('circulating_supply'),
                'total_supply': coin.get('total_supply'),
                'max_supply': coin.get('max_supply'),
                'ath': coin.get('ath'),
                'ath_change_percentage': coin.get('ath_change_percentage'),
                'ath_date': coin.get('ath_date'),
                'atl': coin.get('atl'),
                'atl_change_percentage': coin.get('atl_change_percentage'),
                'atl_date': coin.get('atl_date'),
                'last_updated': coin.get('last_updated')
            })

    logging.info(f"Data successfully written to {csv_file}")

except Exception as e:
    logging.error(f"An error occurred during CSV writing or data processing: {e}")
    exit(1)