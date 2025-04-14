import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load dataset
data = pd.read_csv('Snow-Year.csv')


# print all data (row , column) in csv file

# print("Columns in the dataset:", data.columns)
# print("Complete Dataset:")
# print(data.to_string())

# Debug: Print the column names to verify
print("Columns in the dataset:", data.columns)
print(data.head())

# Define predictor and response variables
X = data['Year']  # Correct column name
y = data['Enso During']  # Correct column name

average_enso = y.mean()
print("Average 'Enso During':", average_enso)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Reshape X to 2D (required for sklearn models)
X_train = X_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# mean_error = (predictions - y_test).mean()
# print("Mean Error:", mean_error)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

# Calculate standard deviation of 'Enso During' column
enso_std_dev = data['Enso During'].std()

# Print the standard deviation
print("Standard Deviation of 'Enso During':", enso_std_dev)

