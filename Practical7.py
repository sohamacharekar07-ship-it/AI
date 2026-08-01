Machine Learning
1. Using any small dataset (e.g., Iris or a CSV dataset), write a Python program to demonstrate the basic machine learning workflow.
a. Load dataset using Pandas.
b. Perform basic preprocessing (handling missing values or scaling).
c. Split dataset into training and testing sets.
d. Train a simple classifier.
e. Display training and testing accuracy.

DATASET - IRIS
pandas as pd
import numpy as np
from sklearn.preprocessing iimport mport LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
Load the Dataset
# 1. Load the Dataset
df = pd.read_csv("iris - iris - iris - iris.csv")
print("========== Dataset Loaded ==========\n")
Display the Dataset
# 2. Display the Dataset
print("First 5 Records:")
print(df.head())

Check Dataset Information
# 3. Check Dataset Information
print("\nDataset Information:")
df.info()

Display Dataset Shape
# 4. Display Dataset Shape
print("\nDataset Shape:")
print(df.shape)

Display Column Names
# 5. Display Column Names
print("\nColumn Names:")
print(df.columns)

Display Summary Statistics
# 6. Display Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

Check Data Types
# 7. Check Data Types
print("\nData Types:")
print(df.dtypes)

Check Missing Values
# 8. Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

Handle Missing Values
# 9. Handle Missing Values
numeric_columns = df.select_dtypes(include=np.number).columns
imputer = SimpleImputer(strategy="mean")
df[numeric_columns] = imputer.fit_transform(df[numeric_columns])
print("\nMissing Values After Handling:")
print(df.isnull().sum())

Remove Duplicate Records
# 10. Remove Duplicate Records
print("\nDuplicate Records Before Removing:")
print(df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicate Records After Removing:")
print(df.duplicated().sum())

Encode Categorical Data (Label Encoding / One-Hot Encoding)
# 11. Encode Categorical Data
encoder = LabelEncoder()
df["species"] = encoder.fit_transform(df["species"])
print("\nEncoded Dataset:")
print(df.head())

Rename Columns
# 12. Rename Columns
df.rename(columns={
    "sepal_length":"Sepal_Length",
    "sepal_width":"Sepal_Width",
    "petal_length":"Petal_Length",
    "petal_width":"Petal_Width",
    "species":"Species"
}, inplace=True)
print("\nColumn Names After Rename:")
print(df.columns)

Drop Unnecessary Columns
# 13. Drop Unnecessary Columns
# Iris dataset has no unnecessary columns.
# Example (if any column existed):
# df.drop(columns=["ID"], inplace=True)
print("\nNo unnecessary columns to drop.")

Select Features (Feature Selection)
# 14. Select Features
features = [
    "Sepal_Length",
    "Sepal_Width",
    "Petal_Length",
    "Petal_Width"
]
print("\nSelected Features:")
print(features)

Create New Features (Feature Engineering)
# 15. Create New Features
df["Petal_Area"] = df["Petal_Length"] * df["Petal_Width"]
print("\nNew Feature Created: Petal_Area")
print(df.head())

Convert Data Types
# 16. Convert Data Types
df["Species"] = df["Species"].astype(int)
print("\nData Types After Conversion:")
print(df.dtypes)

Normalize Data (Min-Max Scaling)
# 17. Normalize Data (Min-Max Scaling)
minmax = MinMaxScaler()
columns_to_scale = features + ["Petal_Area"]
df[columns_to_scale] = minmax.fit_transform(df[columns_to_scale])
print("\nNormalized Data:")
print(df.head())

Standardize Data (Standard Scaling)
# 18. Standardize Data (Standard Scaling)
standard = StandardScaler()
df[columns_to_scale] = standard.fit_transform(df[columns_to_scale])
print("\nStandardized Data:")
print(df.head())

Split Features and Target Variable
# 19. Split Features and Target Variable
X = df[columns_to_scale]
y = df["Species"]
print("\nFeatures (X):")
print(X.head())
print("\nTarget Variable (y):")
print(y.head())





DATASET - PENGUINS
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
Load the Dataset
# 1. Load the Dataset
df = pd.read_csv("penguins.csv")
print("========== Dataset Loaded ==========\n")

Display the Dataset
# 2. Display the Dataset
print("First 5 Records:")
print(df.head())

Check Dataset Information
# 3. Check Dataset Information
print("\nDataset Information:")
df.info()

Display Dataset Shape
# 4. Display Dataset Shape
print("\nDataset Shape:")
print(df.shape)

Display Column Names
# 5. Display Column Names
print("\nColumn Names:")
print(df.columns)

Display Summary Statistics
# 6. Display Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

Check Data Types
# 7. Check Data Types
print("\nData Types:")
print(df.dtypes)

Check Missing Values
# 8. Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

Handle Missing Values
# 9. Handle Missing Values
numeric_columns = df.select_dtypes(include=np.number).columns
imputer = SimpleImputer(strategy="mean")
df[numeric_columns] = imputer.fit_transform(df[numeric_columns])
categorical_columns = df.select_dtypes(include="object").columns
for col in categorical_columns:
    df[col].fillna(df[col].mode()[0], inplace=True)
print("\nMissing Values After Handling:")
print(df.isnull().sum())

Remove Duplicate Records
# 10. Remove Duplicate Records
print("\nDuplicate Records Before Removing:")
print(df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicate Records After Removing:")
print(df.duplicated().sum())

Encode Categorical Data (Label Encoding / One-Hot Encoding)
# 11. Encode Categorical Data
encoder = LabelEncoder()
df["species"] = encoder.fit_transform(df["species"])
df["island"] = encoder.fit_transform(df["island"])
df["sex"] = encoder.fit_transform(df["sex"])
print("\nEncoded Dataset:")
print(df.head())

Rename Columns
# 12. Rename Columns
df.rename(columns={
    "bill_length_mm":"Bill_Length",
    "bill_depth_mm":"Bill_Depth",
    "flipper_length_mm":"Flipper_Length",
    "body_mass_g":"Body_Mass",
    "species":"Species",
    "island":"Island",
    "sex":"Sex"
}, inplace=True)
print("\nColumn Names After Rename:")
print(df.columns)

Drop Unnecessary Columns
# 13. Drop Unnecessary Columns
if "year" in df.columns:
    df.drop(columns=["year"], inplace=True)
print("\nRemaining Columns:")
print(df.columns)

Select Features (Feature Selection)
# 14. Select Features
features = [
    "Bill_Length",
    "Bill_Depth",
    "Flipper_Length",
    "Body_Mass"
]
print("\nSelected Features:")
print(features)

Create New Features (Feature Engineering)
# 15. Create New Feature
df["Bill_Ratio"] = df["Bill_Length"] / df["Bill_Depth"]
print("\nNew Feature Created: Bill_Ratio")
print(df.head())

Convert Data Types
# 16. Convert Data Types
df["Species"] = df["Species"].astype(int)
df["Island"] = df["Island"].astype(int)
df["Sex"] = df["Sex"].astype(int)
print("\nData Types After Conversion:")
print(df.dtypes)

Normalize Data (Min-Max Scaling)
# 17. Normalize Data
columns_to_scale = features + ["Bill_Ratio"]
minmax = MinMaxScaler()
df[columns_to_scale] = minmax.fit_transform(df[columns_to_scale])
print("\nNormalized Data:")
print(df.head())

Standardize Data (Standard Scaling)
# 18. Standardize Data
standard = StandardScaler()
df[columns_to_scale] = standard.fit_transform(df[columns_to_scale])
print("\nStandardized Data:")
print(df.head())

Split Features and Target Variable
# 19. Split Features and Target
X = df[columns_to_scale]
y = df["Species"]
print("\nFeatures (X):")
print(X.head())
print("\nTarget Variable (y):")
print(y.head())

