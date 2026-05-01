from binance.client import Client
from binance.exceptions import BinanceAPIException

class BinanceTestnetClient:
    def __init__(self, api_key, api_secret):
        # We initialize the client
        self.client = Client(api_key, api_secret, testnet=True)
        
        # EXPLICITLY set the Futures URL for the Testnet as per your task instructions
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi/v1'

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                'symbol': symbol.upper(),
                'side': side.upper(),
                'type': order_type.upper(),
                'quantity': quantity,
                'recvWindow': 10000  # Increased from 6000 to 10000
            }
            if order_type.upper() == 'LIMIT':
                params['price'] = str(price)
                params['timeInForce'] = 'GTC'

            # Use the futures_create_order method specifically
            response = self.client.futures_create_order(**params)
            return response
        except BinanceAPIException as e:
            raise Exception(f"Binance API Error: {e.message}")
        except Exception as e:
            raise Exception(f"Connection Error: {str(e)}")