# binance-trading-bot
Python CLI trading bot that places MARKET and LIMIT orders on Binance Futures Testnet with logging, validation, and error handling.
# Binance Futures Testnet Trading Bot
This project is a Python CLI application that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).  
The bot accepts user input from the command line, validates parameters, executes orders using the Binance API, and logs API responses and errors.

The project demonstrates a clean, modular structure with a separate API client layer, order logic, validation, logging, and CLI interface.
---
## Features
- Place MARKET orders on Binance Futures Testnet
- Place LIMIT orders on Binance Futures Testnet
- Supports both BUY and SELL sides
- Command-line interface using `argparse`
- Input validation for order parameters
- Logging of API requests, responses, and errors
- Exception handling for invalid inputs and API errors
- Structured and modular Python code
---
## Project Structure
trading_bot/
│
├── bot/
│ ├── client.py # Binance client wrapper
│ ├── orders.py # Order placement logic
│ ├── validators.py # Input validation
│ └── logging_config.py # Logging setup
│
├── cli.py # CLI entry point
├── requirements.txt
├── README.md
└── trading_bot.log

---
## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/binance-trading-bot.git
cd binance-trading-bot
2. Install Dependencies
pip install -r requirements.txt
3. Create Environment Variables
Create a .env file in the project root and add your Binance Testnet API credentials.
API_KEY=your_api_key
API_SECRET=your_secret_key
You can generate API credentials from the Binance Futures Testnet dashboard.

Example Usage
Place a MARKET Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
Place a LIMIT Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 71000
Output Example
Order Request Summary
----------------------
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.002

Order Response
----------------------
Order ID: 12652965931
Status: NEW
Executed Quantity: 0.000
Logging

All API responses, requests, and errors are logged in:
trading_bot.log

Example logged events include:
Successful order placements

API errors
Request details
Response payloads
Assumptions
This bot uses Binance Futures Testnet, not real trading.
Valid Binance API credentials are required.
Orders must satisfy Binance minimum notional value requirements.

Notes
-----
This project was developed as part of a Python Developer technical assessment to demonstrate:
Python API integration
CLI application development
Structured project design
Logging and error handling
