## linear regression
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import scipy 
# import seaborn as sns
# import statsmodels.api as sm
# import statsmodels.formula.api as smf

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample stock price data (for demonstration purposes)
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Price': np.random.rand(100) * 100 + 100  # Simulated stock prices
}

df = pd.DataFrame(data)

# Feature engineering
df['Date'] = pd.to_datetime(df['Date'])
df['Day'] = df['Date'].dt.dayofweek  # Extract day of the week as a feature

# Split data into training and testing sets
X = df[['Day']]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Visualize the results
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.xlabel('Day of the Week')
plt.ylabel('Stock Price')
plt.title('Stock Price Prediction')
plt.show()

