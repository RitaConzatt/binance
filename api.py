from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
import time

# Function to get the current price of a specified symbol
def get_price(symbol):
    """
    Retrieves the current price of a specified symbol on the Binance exchange.

    :param symbol: The trading pair symbol (e.g., 'XMRUSDT')
    :return: Current price if successful, None otherwise
    """
    try:
        # Fetch the current ticker price for the symbol
        ticker = client.get_symbol_ticker(symbol=symbol)
        return ticker['price']
    except BinanceAPIException as e:
        print(f"Binance API Exception occurred: {e.status_code} - {e.message}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None


# Function to get the quantity of a specified asset in your account
def get_quantity(asset):
    """
    Retrieves the quantity of a specified asset in the Binance account.

    :param asset: The asset symbol (e.g., 'XMR')
    :return: Quantity of the asset if successful, None otherwise
    """
    try:
        # Fetch account information
        account_info = client.get_account()
        # Extract the balance for the specified asset
        balance = next((item for item in account_info['balances'] if item['asset'] == asset), None)
        return balance['free'] if balance else '0'
    except BinanceAPIException as e:
        print(f"Binance API Exception occurred: {e.status_code} - {e.message}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None


# Function to place a limit sell order
def sell_limit(symbol, quantity, price):
    """
    Places a limit sell order on the Binance exchange.

    :param symbol: The trading pair (e.g., 'XMRUSDT')
    :param quantity: The amount of the asset to sell
    :param price: The price at which to sell the asset
    :return: Order information if successful, None otherwise
    """
    try:
        order = client.create_order(
            symbol=symbol,
            side=Client.SIDE_SELL,
            type=Client.ORDER_TYPE_LIMIT,
            timeInForce=Client.TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=str(price)
        )
        print(f"Limit sell order placed: {order}")
        return order
    except BinanceAPIException as e:
        print(f"Binance API Exception occurred: {e.status_code} - {e.message}")
    except BinanceOrderException as e:
        print(f"Binance Order Exception occurred: {e.status_code} - {e.message}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

# Function to place a limit buy order
def buy_limit(symbol, quantity, price):
    """
    Places a limit buy order on the Binance exchange.

    :param symbol: The trading pair (e.g., 'BTCUSDT')
    :param quantity: The amount of the asset to buy
    :param price: The price at which to buy the asset
    :return: Order information if successful, None otherwise
    """
    try:
        order = client.create_order(
            symbol=symbol,
            side=Client.SIDE_BUY,
            type=Client.ORDER_TYPE_LIMIT,
            timeInForce=Client.TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=str(price)
        )
        print(f"Limit buy order placed: {order}")
        return order
    except BinanceAPIException as e:
        print(f"Binance API Exception occurred: {e.status_code} - {e.message}")
    except BinanceOrderException as e:
        print(f"Binance Order Exception occurred: {e.status_code} - {e.message}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

# Your Binance API credentials
api_key = 'xxxxxxx'
api_secret = 'xxxxxxx'

# Initialize the Binance client
client = Client(api_key, api_secret)

# Main function
def main():


    while True:
        result = sell_limit('BNBUSDT', 1, 0.25)
        if result is not None:
            print("sold")
            break
        else:
            print("trying...")
            time.sleep(0.2)  



if __name__ == "__main__":
    main()

