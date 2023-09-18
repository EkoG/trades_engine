from trades.trade_engine import TradeEngine
from IPython.display import display

if __name__ == '__main__':
    today_trades = TradeEngine('trades/trades.csv')
    # Volume of operations: sum of all values sell and buys
    display(today_trades.volume())
    # Check for all logarithmic traders, you can select the limit of operation this is CALCULATED PER DAY
    display(today_trades.algo_traders(3))
    # Average price of all values by ticket
    display(today_trades.average_price())
    # List of trades selected by ticker and date
    display(today_trades.list_trades('GOOGL', '2023-08-02'))
