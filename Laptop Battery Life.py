import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

# Load the dataset
dataset = pd.read_csv('trainingdata.txt', header=None)  # Updated path

# Plot the graph with the data
plt.plot(dataset.iloc[:, 0], dataset.iloc[:, 1], 'ro')
plt.xlabel('Charging Time')
plt.ylabel('Laptop Battery Life')
plt.show()

# Remove items with a duration of time greater than eight
dataset = dataset[dataset.iloc[:, 1] < 8]

# Add bias (intercept term)
dataset.insert(0, 'bias', 1)

# Separate independent and dependent variables
X = dataset.iloc[:, [0, 1]].values
Y = dataset.iloc[:, 2].values

# Create the classifier model
model = linear_model.LinearRegression()
model.fit(X, Y)

# Set new value to predict
timeCharged = float(input().strip())
result = model.predict([[1, timeCharged]])  # Bias term is 1

# Cap the predicted value at 8 and print the result rounded to 2 decimal places
predicted_life = min(result[0], 8.0)
print(round(predicted_life, 2))
