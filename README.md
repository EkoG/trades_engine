# Trade engine excersice
# I suggest to use Python-Pandas to solve this excersie

Trade Analysis Engine
Python Coding Challenge for Sidepocket
You have just been handed raw trade data in the form of a CSV file. Your task is to build a trade
analysis engine that provides insights into the trade patterns and aids in identifying potential
discrepancies.
CSV File Format:
trade_id, customer_id, trade_date, ticker, trade_type, quantity, price
1001, C123, 2023-08-01, AAPL, BUY, 100, 150
1002, C124, 2023-08-02, GOOGL, SELL, 50, 2700
trade_id: A unique identifier for each trade.
customer_id: Identifier for the customer.
trade_date: Date of the trade.
ticker: Ticker symbol of the stock.
trade_type: Type of trade - either BUY or SELL.
quantity: Number of shares traded.
price: Price of the stock at the time of the trade.
Tasks:|
Load the CSV data.
Calculate the total buying and selling volume for each ticker.
Identify any customers that have more than 3 trades in a single day. This could indicate
algorithmic trading or potential discrepancies.
Calculate the average price for each ticker on days it was traded.
Given a ticker and a date, return the list of trades for that ticker on the provided date.
Constraints:
The CSV data will contain at least 1 trade and at most 10,000 trades.
Deliverables:
Python code for the tasks.
Brief explanation for the solutions.
Note: This project is for evaluation purposes only and won't be used for any other
purpose without your express permission. The project is intended to be completed
individually and should reflect your own work and ideas.
