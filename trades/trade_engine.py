#!/usr/bin/python3
import pandas as pd


class TradeEngine:
    def __init__(self, file: str) -> None:
        # Date today
        """
        Instead of using the date from today, the date will be hardcoded. But if the script will run
        in a different environment I suggest using datetime.today()
        """
        # self.date_now = datetime.today()
        self.date = '2023-08-02'
        # Load file
        """
        To complete this task I suggest to use pandas to analyse data 
        """
        self.trades = pd.read_csv(file)

    def volume(self) -> pd.DataFrame:
        # Calculate the total buying and selling volume for each ticker
        """
        To calculate each column I grouped by ticker them sum each column and finally rename quantity to
        volume
        """
        volumes = self.trades.groupby("ticker").sum().rename(columns={'quantity': 'volume'})
        return volumes[['volume']]

    def algo_traders(self, trade_limit: int) -> pd.DataFrame:
        # Identify any customers that have more than 3 trades in a single day. This could indicate
        # algorithmic trading or potential discrepancies

        """
        To Indentify any customer with more than 3 trades we count the trades of each trader then filter
        and finally display them
        """
        # Date is hardcoded on line 13 CHECK FOR DIFFERENT DATE if need it
        trades = self.trades.loc[self.trades['trade_date'] == self.date]
        # Count each of the values for the rows in the DataFrame (DF)
        # Value counts method return a Series not a DF
        count_trades = trades['customer_id'].value_counts()
        # Create a new dataFrame using reset index and rename for the counts
        num_trades = count_trades.reset_index().rename(columns={"index": "customer_id", 0: "count"})
        # Filter the number of operations (trades) you want i.e. trader with more than 3 operations will be listed
        idx = count_trades[count_trades <= trade_limit]
        # Return the list of values
        alg_traders = num_trades[~num_trades['count'].isin(idx)]
        return alg_traders

    def average_price(self) -> pd.DataFrame:
        # Calculate the average price for each ticker on days it was traded.
        """To calculate the average we group by ticker, and then we use mean on price column """
        avg_prices = self.trades.groupby('ticker', as_index=False)['price'].mean()
        return avg_prices

    def list_trades(self, ticker: str, date: str) -> pd.DataFrame:
        # Given a ticker and a date, return the list of trades for that ticker on the provided date.
        data = self.trades.loc[(self.trades['ticker'] == ticker) & (self.trades['trade_date'] == date)]
        return data

    """
    I added two methods to return dataFrame to csv file or to dictionary. Instead of returning a DF 
    you could return a Json (dictionary) format or CSV.
    """

    @staticmethod
    def to_csv(df: pd.DataFrame) -> object:
        return df.to_csv()

    @staticmethod
    def to_dict(df: pd.DataFrame) -> object:
        return df.to_dict()
    