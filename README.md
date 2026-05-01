🚀 Binance Futures Testnet Trading Bot
A python based CLI trading bot that allows users to place MARKET and LIMIT orders on the Binance Futures Testnet.

📌 Overview
This project demonstrates a simple automated trading workflow using Binance Futures Testnet APIs. It supports real-time order placement with proper validation and logging.

📌 Features
✅ Place BUY / SELL orders
✅ Supports MARKET and LIMIT orders
✅ Command-line interface (CLI-based execution)
✅ Input validation for order types
✅ Logging for success and error handling
✅ Clean modular structure

📦 Requirements
Create a requirements.txt file with:
python-binance
requests

📂 Project Structure
.
├── cli.py
├── bot/
│   ├── client.py
│   ├── logging_config.py
├── requirements.txt
├── README.md

1️⃣ Clone the Repository
git clone https://github.com/your-username/binance-futures-trading-bot.git
cd binance-futures-trading-bot

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure API Keys
Edit cli.py and replace:
API_KEY = "YOUR_TESTNET_API_KEY"
API_SECRET = "YOUR_TESTNET_API_SECRET"

▶️ How to Run
✅ MARKET Order Example
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001

Example Logs
📄 MARKET Order Log
INFO: Sending MARKET BUY order for 0.001 BTCUSDT
INFO: SUCCESS: Order ID 1874563

✅ LIMIT Order Example
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 30000

LIMIT Order Log
INFO: Sending LIMIT SELL order for 0.001 BTCUSDT
INFO: SUCCESS: Order ID 800004

This implementation reflects my ability to build clean, functional systems with real-world API integration, and I look forward to extending it with advanced trading strategies and automation.
