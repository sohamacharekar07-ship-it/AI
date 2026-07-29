#1. Using a small dataset (e.g., weather or spam dataset), implement a Naive Bayes
#classifier using scikit-learn.
#CODE:
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Overcast'],
    'Temperature': ['Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool'],
    'Humidity': ['High', 'High', 'High', 'Normal', 'Normal', 'Normal'],
    'Windy': ['False', 'True', 'False', 'False', 'True', 'True'],
    'Play': ['No', 'No', 'Yes', 'Yes', 'No', 'Yes']
}
df = pd.DataFrame(data)
le = LabelEncoder()
columns = ['Outlook', 'Temperature', 'Humidity', 'Windy', 'Play']
for col in columns:
    df[col] = le.fit_transform(df[col])
X = df[['Outlook', 'Temperature', 'Humidity', 'Windy']]
y = df['Play']
model = GaussianNB()
model.fit(X, y)
# Test data with column names
test = pd.DataFrame(
    [[2, 1, 0, 1]],
    columns=['Outlook', 'Temperature', 'Humidity', 'Windy']
)
prediction = model.predict(test)
if prediction[0] == 1:
    print('Prediction: Yes, we can play')
else:
    print('Prediction: No, we cannot play')
print("Soham Acharekar T001")

