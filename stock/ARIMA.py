# import pandas as pd
# import matplotlib.pyplot as plt
# from statsmodels.tsa.arima_model import ARIMA
# from matplotlib import pyplot as plt
# import yfinance as yf
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split


# # Define the stock symbol
# symbol = "AAPL"  # Apple Inc.

# # Fetch live stock data
# stock_data = yf.Ticker(symbol)
# # live_data = stock_data.history(period="1d")
# # live_data = stock_data.history(start="2023-10-01", end="2023-11-02")


# # Date = pd.date_range(start='2023-10-01',end='2023-11-02')


# start_date = "2023-01-01"
# end_date = "2023-11-01"

# df = yf.download(symbol, start=start_date, end=end_date)

# df = df.reset_index()

# # Load historical stock price data into a DataFrame (ensure date is in datetime format)
# # df = pd.read_csv('stock_data.csv')
# # df['Date'] = pd.to_datetime(df['Date'])

# # Split the data into training and testing sets
# train_size = int(len(df) * 0.8)
# train_data, test_data = df[:train_size], df[train_size:]

# # Create and train an ARIMA model
# model = ARIMA(train_data['Close'], order=(5, 1, 0))
# model_fit = model.fit(disp=0)

# # Make predictions
# predictions = model_fit.forecast(steps=len(test_data))

# # Visualize the actual and predicted stock prices
# plt.plot(test_data['Date'], test_data['Close'], label='Actual Stock Price')
# plt.plot(test_data['Date'], predictions, color='red', label='Predicted Stock Price')
# plt.legend()
# plt.title('Stock Price Prediction')
# plt.xlabel('Date')
# plt.ylabel('Close')
# plt.show()


from datetime import datetime

# Specify the date
date_str = "2023-11-03"

# Convert the date string to a datetime object
date_obj = datetime.strptime(date_str, "%Y-%m-%d")

# Calculate the Unix timestamp (seconds since January 1, 1970)
timestamp = (date_obj - datetime(1970, 1, 1)).total_seconds()

# Convert the timestamp to a float
timestamp_float = float(timestamp)

print(timestamp_float)

import matplotlib.pyplot as plt

import yfinance as yf
import pandas as pd
pd.options.plotting.backend = "plotly"

# taking the close price (end of day)
sp500_data = yf.download('^GSPC', start="1980-01-01", end="2023-11-01")
sp500_data = sp500_data[['Close']]
# sp500_data.plot(figsize=(12, 12))
fig = sp500_data.plot()
fig.show()
print(type(sp500_data))



# import numpy as np
# from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt

# # Generate synthetic data for demonstration
# np.random.seed(0)
# X = 2 * np.random.rand(100, 1)  # Independent variable
# y = 4 + 3 * X + np.random.randn(100, 1)  # Dependent variable with some noise

# # Create a LinearRegression model
# model = LinearRegression()

# # Fit the model to the data
# model.fit(X, y)

# # Get the model parameters
# intercept = model.intercept_[0]
# slope = model.coef_[0][0]

# # Make predictions
# X_new = np.array([[0], [2]])
# y_pred = model.predict(X_new)

# print(y_pred)

# # Visualize the data and regression line
# plt.scatter(X, y, label="Data Points")
# plt.plot(X_new, y_pred, "r-", label="Regression Line")
# plt.xlabel("Independent Variable (X)")
# plt.ylabel("Dependent Variable (y)")
# plt.legend()
# plt.show()

# # Print the model parameters
# print("Intercept (b0):", intercept)
# print("Slope (b1):", slope)
