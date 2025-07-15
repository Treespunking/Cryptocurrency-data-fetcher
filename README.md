# Cryptocurrency-Data-Fetcher
## Market Information Retrieval from the CoinGecko API

## Purpose
The script fetches comprehensive cryptocurrency market data for a predefined list of coins and saves it in a structured CSV file for analysis or reporting purposes.

## Key Components

**Data Source**: Uses CoinGecko's `/coins/markets` API endpoint to retrieve real-time cryptocurrency market data.

**Input**: Reads cryptocurrency IDs from a file called `output_ids.txt` (one ID per line).

**Authentication**: Uses an API key stored in environment variables via a `.env` file for authenticated requests.

**Batch Processing**: Implements intelligent batching to handle large numbers of cryptocurrencies efficiently:
- Processes coins in batches of 200
- Includes rate limiting (2-second delays between requests)
- Handles API limitations gracefully

**Data Fields**: Captures 24 different metrics for each cryptocurrency, including:
- Basic info (id, symbol, name)
- Price data (current price, 24h changes)
- Market metrics (market cap, volume, rank)
- Supply information (circulating, total, max supply)
- Historical data (all-time high/low, dates)

**Error Handling**: Comprehensive error management with logging for:
- Missing files or API keys
- API request failures
- Data processing errors

**Output**: Creates a well-structured CSV file (`crypto_data.csv`) with all fetched data.

## Use Cases
This script would be useful for:
- Cryptocurrency portfolio tracking
- Market analysis and research
- Building cryptocurrency dashboards
- Data collection for trading algorithms
- Regular market monitoring and reporting

The script is production-ready with proper logging, error handling, and follows best practices for API consumption with rate limiting.
