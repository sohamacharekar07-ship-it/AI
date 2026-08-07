4. Implement k-fold cross-validation on a classification model.
CODE:(iris dataset)
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
# Load dataset
iris = load_iris()
X = iris.data
y = iris.target
# Create classification model
model = KNeighborsClassifier()
# Apply 5 fold cross-validation
scores = cross_val_score(model, X, y, cv=5)
print("Accuracy scores for each fold:")
print(scores)
print("Average Accuracy:", round(scores.mean() * 100, 2), "%")
OUTPUT:

CODE:(netflix dataset)
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
# Load dataset
netflix = pd.read_csv("NetFlix - NetFlix.csv")
# Convert categorical columns to numeric
label_encoder = LabelEncoder()
netflix["director"] = label_encoder.fit_transform(netflix["director"].astype(str))
netflix["country"] = label_encoder.fit_transform(netflix["country"].astype(str))
netflix["rating"] = label_encoder.fit_transform(netflix["rating"].astype(str))
# Features and target
X = netflix[["director", "country", "rating"]]
y = label_encoder.fit_transform(netflix["type"])
# Create classification model
model = KNeighborsClassifier()
# Apply 5-fold cross-validation
scores = cross_val_score(model, X, y, cv=5)
print("Accuracy scores for each fold:")
print(scores)
print("Average Accuracy:", round(scores.mean() * 100, 2), "%")
OUTPUT:

5. Implement a Decision Tree classifier using the Iris or any relevant dataset.
CODE:(iris dataset)
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
# Load dataset
iris = load_iris()
X = iris.data
y = iris.target
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=1
)
# Create model
model = DecisionTreeClassifier()
# Train model
model.fit(X_train, y_train)
# Display accuracy
print("Training Accuracy:", model.score(X_train, y_train) * 100)
print("Testing Accuracy:", model.score(X_test, y_test) * 100)
# Prediction
prediction = model.predict([X_test[0]])
print("Predicted Class:", prediction[0])
OUTPUT:

CODE:(netflix dataset)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
# Load dataset
netflix = pd.read_csv("NetFlix - NetFlix.csv")
# Convert categorical data into numerical values
label_encoder = LabelEncoder()
netflix["director"] = label_encoder.fit_transform(netflix["director"].astype(str))
netflix["country"] = label_encoder.fit_transform(netflix["country"].astype(str))
netflix["rating"] = label_encoder.fit_transform(netflix["rating"].astype(str))
netflix["type"] = label_encoder.fit_transform(netflix["type"])
X = netflix[["director", "country", "rating"]]
y = netflix["type"]
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=1
)
# Create model
model = DecisionTreeClassifier()
# Train model
model.fit(X_train, y_train)
# Display accuracy
print("Training Accuracy:", model.score(X_train, y_train) * 100)
print("Testing Accuracy:", model.score(X_test, y_test) * 100)
# Prediction
prediction = model.predict([X_test.iloc[0]])
print("Predicted Class:", prediction[0])
OUTPUT:

