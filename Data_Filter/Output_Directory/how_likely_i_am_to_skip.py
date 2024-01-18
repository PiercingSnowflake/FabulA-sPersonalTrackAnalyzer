import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from scipy.stats import mode
import numpy as np

# Load the data
with open("RealResult.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Specify the target variable and features
target_variable = "skipped"
features = ["danceability", "energy", "loudness", "mode", "speechiness",
            "acousticness", "instrumentalness", "liveness", "valence", "tempo"]

# Handle missing values
df = df.dropna(subset=[target_variable])  # Drop rows where the target variable is missing

# Assuming 'features' is a list of columns you want to fill missing values for
for feature in features:
    mode_values = mode(df[feature].dropna())[0]
    if isinstance(mode_values, np.ndarray) and len(mode_values) > 0:
        mode_value = mode_values[0]
        df[feature] = df[feature].fillna(mode_value)



# Convert boolean values to numeric (True: 1, False: 0)
df[target_variable] = df[target_variable].astype(int)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target_variable], test_size=0.2, random_state=42)

# Train a Random Forest Classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
