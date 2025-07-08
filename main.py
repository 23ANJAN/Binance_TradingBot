import os

bot = BasicBot(API_Key, Secret_Key)

print("Welcome to the Binance Testnet Trading Bot")

symbol = input("Enter trading pair : ").upper()
side = input("Buy or Sell: ").upper()
order_type = input("Order Type (market/limit): ").lower()
quantity = float(input("Quantity: "))

if order_type == "market":
    result = bot.place_market_order(symbol, side, quantity)

elif order_type == "limit":
    price = input("Enter Limit Price: ")
    result = bot.place_limit_order(symbol, side, quantity, price)

else:
    print("Invalid order type selected.")
    result = {"error": "Invalid input"}

print("Order Result:", result)
