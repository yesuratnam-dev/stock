from matplotlib import pyplot as plt
import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# Define the stock symbol
symbol = "AAPL"  # Apple Inc.

# Fetch live stock data
stock_data = yf.Ticker(symbol)
# live_data = stock_data.history(period="1d")
# live_data = stock_data.history(start="2023-10-01", end="2023-11-02")


# Date = pd.date_range(start='2023-10-01',end='2023-11-02')


start_date = "2023-01-01"
end_date = "2023-11-01"

df = yf.download(symbol, start=start_date, end=end_date)

df = df.reset_index()

print(df.columns)




# df['Date'] = pd.to_datetime(df['Date'])
# df['Day'] = df['Date'].dt.dayofweek 

# X = df['Date']

df['Date'] = pd.to_datetime(df['Date'])
df['Day'] = df['Date'].dt.dayofweek  # Extract day of the week as a feature

# Split data into training and testing sets
# X = df[['Date']]
X = df[['Date']].values.astype("float64")
y = df['Close']

# print(X)    
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=42)

model = LinearRegression()


model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

val = X_test[[2]]


y_man_pred = model.predict(val)
print(y_man_pred)

# # Visualize the results

pd.options.plotting.backend = "plotly"

plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.xlabel('Day of the Week')
plt.ylabel('Stock Price')
plt.title('Stock Price Prediction')
# plt.show()


# print(live_data)