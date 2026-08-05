Q.1 Linear Regression Problem
Given data of house area (in sq.ft.) and corresponding price (in lakhs):
Area: 600, 800, 1000, 1200, 1400, 1600
Price: 32, 40, 49, 58, 68, 79
Tasks:
1. Find the regression equation of price on area.
2. Predict the price of a 1500 sq.ft. house.
3. Predict the price of a 2500 sq.ft. house.
import numpy as np
from sklearn.linear_model import LinearRegression

# Data
area = np.array([600,800,1000,1200,1400,1600]).reshape(-1,1)
price = np.array([32,40,49,58,68,79])

# Model
model = LinearRegression()
model.fit(area, price)

# Equation
m = model.coef_[0]
c = model.intercept_

print("Regression Equation: y =", m, "x +", c)

# Predictions
print("\nPrice for 1500 sq.ft:", model.predict([[1500]])[0])
print("Price for 2500 sq.ft:", model.predict([[2500]])[0])
Q.2 A company has collected the following employee data:
• Employee ID
• Employee Age
• Years of Experience
• Salary
You need to develop a Linear Regression model to predict an employee's salary.
Tasks
1. Identify the independent variable (X) and the dependent variable (Y).
2. Explain why you selected these variables.
3. Create a Pandas DataFrame using the given data.
4. Split the dataset into training and testing sets.
5. Train a Linear Regression model.
6. Predict the salary for an employee having 7 years of experience.
7. Display:

o Slope (Coefficient)
o Intercept
o R2 Score
8. Plot the regression line.
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create dataset
data = pd.DataFrame({
    'Experience':[1,2,3,4,5,6,8,10],
    'Salary':[25000,30000,35000,40000,45000,50000,60000,70000]
})

# Variables
X = data[['Experience']]
y = data['Salary']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Predict for 7 years
pred = model.predict([[7]])

print("Predicted Salary:", pred[0])
print("\nCoefficient:", model.coef_[0])
print("\nIntercept:", model.intercept_)
print("\nR2 Score:", model.score(X_test, y_test))

# Plot
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()
Q.3 
1. California Housing Dataset
Problem Statement
A real estate company wants to predict the median house value based on housing features.
Features
• Median Income
• House Age
• Average Rooms
• Average Bedrooms
• Population
• Average Occupancy
• Latitude
• Longitude
Target
Median House Value
Tasks
1. Load the dataset using Pandas.
2. Display the first five records.
3. Check for missing values.
4. Select one suitable feature (e.g., Median Income) as the independent variable.
5. Split the dataset into training and testing sets.
6. Train a Linear Regression model.

7. Predict the house prices.
8. Display:
o Coefficient
o Intercept
o R2 Score
9. Plot the regression line.
10. Interpret the results.
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
# 1. Load the dataset using Pandas
data = pd.read_csv("housing.csv")
# Display column names
print("Columns in Dataset:")
data.columns
# Create required features
data["AveRooms"] = data["total_rooms"] / data["households"]
data["AveBedrms"] = data["total_bedrooms"] / data["households"]
data["AveOccup"] = data["population"] / data["households"]
# Rename columns
data = data.rename(columns={
    "median_income": "MedInc",
    "housing_median_age": "HouseAge",
    "population": "Population",
    "latitude": "Latitude",
    "longitude": "Longitude",
    "median_house_value": "MedHouseVal"
})
# 2. Display the first five records
print("\nFirst Five Records:")
data.head()
# 3. Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Remove missing values (if any)
data = data.dropna()
# 4. Select one suitable feature (Median Income)
X = data[["MedInc"]]
y = data["MedHouseVal"]
# 5. Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=1
)
# 6. Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
# 7. Predict the house prices
y_pred = model.predict(X_test)
# 8. Display Coefficient, Intercept and R2 Score
print("\nCoefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
print("R2 Score:", r2_score(y_test, y_pred))
# 9. Plot the regression line
plt.figure(figsize=(8,6))
plt.scatter(X_test, y_test, color="blue", label="Actual House Prices")
plt.plot(X_test, y_pred, color="red", linewidth=2, label="Regression Line")
plt.xlabel("Median Income")
plt.ylabel("Median House Value")
plt.title("California Housing Dataset - Linear Regression")
plt.legend()
plt.show()
# 10. Interpretation
print("\nInterpretation:")
print("1. The coefficient indicates the change in house value for a one-unit increase in Median Income.")
print("2. The intercept is the predicted house value when Median Income is zero.")
print("3. The R2 Score indicates how well the model fits the data.")
print("4. A higher R2 Score means better prediction accuracy.")

Q.1 Modify the program to detect Digit 7 vs Not Digit 7 instead of Digit 5 vs Not Digit 5.
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset
digits = load_digits()

# Input and Output
X = digits.data
y = (digits.target == 7)   # Digit 7

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

# Train
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Prediction (first sample)
prediction = model.predict([X_test[0]])

if prediction[0]:
    print("Digit is 7")
else:
    print("Digit is not 7")
Q.2 Modify the program to detect Digit 0 vs Not Digit 0.
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

digits = load_digits()

X = digits.data
y = (digits.target == 0)   # Digit 0

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

prediction = model.predict([X_test[0]])

if prediction[0]:
    print("Digit is 0")
else:
    print("Digit is not 0")
Q.3 Modify the program to detect Digit 9 vs Not Digit 9.
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

digits = load_digits()

X = digits.data
y = (digits.target == 9)   # Digit 9

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

prediction = model.predict([X_test[0]])

if prediction[0]:
    print("Digit is 9")
else:
    print("Digit is not 9")
Q.4 Modify the program to display the first 20 predictions instead of only one prediction.
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

digits = load_digits()

X = digits.data
y = (digits.target == 5)   # Digit 5

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# First 20 predictions
predictions = model.predict(X_test[:20])

for i, pred in enumerate(predictions):
    if pred:
        print(f"Sample {i+1}: Digit is 5")
    else:
        print(f"Sample {i+1}: Digit is not 5")
