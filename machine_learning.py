from sklearn.linear_model import LinearRegression
import numpy as np

# Training data
X = np.array([[1], [2], [3], [4]])
y = np.array([1, 3, 5, 7])

# Create and train the model
model = LinearRegression().fit(X, y)

# Print the slope and intercept
print(f"Slope: {model.coef_[0]}, Intercept: {model.intercept_}")

# Predict a new value
prediction = model.predict(np.array([[5]]))
print(f"Prediction for input 5: {prediction[0]}")
