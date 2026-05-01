import argparse
import sys
import os

# This line tells Python to look in the current folder for the 'bot' folder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Change these lines:
from bot.client import BinanceTestnetClient
from bot.logging_config import setup_logging
import logging

# Paste your actual keys here for testing
API_KEY = "YOUR_TESTNET_API_KEY"
API_SECRET = "YOUR_TESTNET_API_SECRET"

def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=['BUY', 'SELL'])
    parser.add_argument("--type", required=True, choices=['MARKET', 'LIMIT'])
    parser.add_argument("--qty", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    if args.type == 'LIMIT' and not args.price:
        logger.error("Price is required for LIMIT orders.")
        return

    client = BinanceTestnetClient(API_KEY, API_SECRET)

    try:
        logger.info(f"Sending {args.type} {args.side} order for {args.qty} {args.symbol}")
        response = client.place_order(args.symbol, args.side, args.type, args.qty, args.price)
        logger.info(f"SUCCESS: Order ID {response.get('orderId')}")
        print(response)
    except Exception as e:
        logger.error(f"FAILED: {e}")

if __name__ == "__main__":
    main()