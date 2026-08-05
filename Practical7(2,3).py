#2
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# Load dataset
data = pd.read_csv("student_marks.csv")
# Input and output (use YOUR column names)
X = data[['study_hours']]
y = data['student_marks']
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=1
)
# Train model
model = LinearRegression()
model.fit(X_train, y_train)
# Display accuracy
print("Training Accuracy:",
      round(model.score(X_train, y_train)*100,2))

print("Testing Accuracy:",
      round(model.score(X_test, y_test)*100,2))
# Predict marks for 11 study hours
new_data = pd.DataFrame([[11]], columns=['study_hours'])
pred = model.predict(new_data)

print("Predicted Marks for 11 hours:",
      round(pred[0],2))

print("Soham Acharekar T001");

#3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
# Load your dataset
data = pd.read_csv("mnist.csv")
# Features and target
X = data.drop("label", axis=1)
y = data["label"]
# Convert target to integer
y = y.astype(int)
# Binary classification: 5 vs NOT 5
y = (y == 5)
# Scale features (important)
scaler = StandardScaler()
X = scaler.fit_transform(X)
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)
# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
# Accuracy
print("Training Accuracy:", model.score(X_train, y_train) * 100)
print("Testing Accuracy:", model.score(X_test, y_test) * 100)
# Predict first test sample
prediction = model.predict([X_test[0]])

if prediction[0]:
    print("Digit is 5")
else:
    print("Digit is NOT 5")
print("Soham Acharekar T001");
y = (digits.target == 7)

