# Crypto Market Data Fetcher

A reliable Python script to fetch cryptocurrency market data from **CoinGecko API** in batches, with robust error handling and CSV export. Ideal for market research, portfolio analysis, and blockchain analytics.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![CoinGecko](https://img.shields.io/badge/API-CoinGecko-green)
![CSV](https://img.shields.io/badge/Output-CSV-blueviolet)

---

## Features
- Fetches live market data for **hundreds of cryptocurrencies** using CoinGecko API
- Supports batched requests to respect rate limits and improve performance
- Reads coin IDs from a text file (`output_ids.txt`) for easy configuration
- Outputs clean, structured **CSV file** with essential metrics
- Includes comprehensive logging to `app.log`
- Built-in delays to avoid API throttling
- Environment variables for secure API key management

---

## Requirements
- Python 3.8+
- Active internet connection
- CoinGecko API key (free tier supported via `x-cg-demo-api-key`)

---

## Setup & Installation

### 1. Clone the repo
```bash
git clone 
cd 
```

### 2. Set up virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

> If you don’t have a `requirements.txt`, create one with:
```txt
requests
python-dotenv
```

### 4. Add your API key in `.env`
```env
COINGECKO_API_KEY=your_coingecko_api_key_here
```
> Never commit this file! It should be in `.gitignore`.

### 5. Prepare coin IDs list
Create `output_ids.txt` with one CoinGecko coin ID per line:
```
bitcoin
ethereum
cardano
solana
polkadot
...
```
> You can get IDs from: https://api.coingecko.com/api/v3/coins/list

### 6. Run the script
```bash
python scrip.py
```

Output will be saved to `crypto_data.csv`  
Logs will be written to `app.log`

---

## Output Fields (CSV)
The following market data fields are included:
- `id`, `symbol`, `name`
- `current_price`, `market_cap`, `market_cap_rank`
- `fully_diluted_valuation`, `total_volume`
- 24h High / Low prices and changes
- Price & market cap change percentages
- Supply data: circulating, total, max
- All-Time High (ATH) and All-Time Low (ATL) values and dates
- `last_updated` timestamp

---

## Project Structure
```
crypto-data-fetcher/
│
├── scrip.py               # Main script
├── output_ids.txt         # List of CoinGecko coin IDs
├── crypto_data.csv        # Output CSV file (generated)
├── app.log                # Log file (generated)
├── requirements.txt       # Dependencies
└── .env                   # Environment variables (ignored)
```

---

## Error Handling & Logging
- Validates presence of required files and API key
- Logs all steps, errors, and warnings to `app.log`
- Handles HTTP errors and empty responses gracefully
- Exits cleanly on critical failures

---

## Use Cases
- Cryptocurrency market research
- Portfolio tracking and benchmarking
- Data pipeline input for dashboards
- Historical analysis when run periodically

---
