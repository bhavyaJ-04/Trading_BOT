🚀 Binance Futures Testnet Trading Bot

A simple command-line trading bot built using Python that allows users to place MARKET and LIMIT orders on the Binance Futures Testnet.

📌 Features
✅ Place BUY / SELL orders
✅ Supports MARKET and LIMIT orders
✅ Command-line interface (CLI-based execution)
✅ Input validation for order types
✅ Logging for success and error handling
✅ Clean modular structure

1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Add API Keys
Open cli.py and replace: 
API_KEY = "YOUR_TESTNET_API_KEY"
API_SECRET = "YOUR_TESTNET_API_SECRET"

Run the bot using CLI
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001

