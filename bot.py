!pip install python-binance    #installing the module binance

from binance.client import Client 
import logging
import time 

API_Key = 'get api'
Secret_Key = 'get api'

class BasicBot:
      def __init__(self,API_Key,Secret_Key, testnet=True ):
        self.client = Client(API_Key,Secret_Key)
        if testnet:
          self.client.futures_URL='https://testnet.binance.vision/api'
        logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )
            logging.info(f"Market Order Placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Market Order Error: {str(e)}")
            return {"error": str(e)}

def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='LIMIT',
                quantity=quantity,
                price=price,
                timeInForce='GTC'
            )
            logging.info(f"Limit Order Placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Limit Order Error: {str(e)}")
            return {"error": str(e)}
