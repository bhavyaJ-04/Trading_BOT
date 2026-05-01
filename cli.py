Install Dependencies: pip install -r requirements.txt
Configure Keys:
Add your API_KEY and API_SECRET to cli.py
Run Commands:
Market Order: python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001
Limit Order: python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 90000

Logging: All activity is recorded in bot_activity.log.
