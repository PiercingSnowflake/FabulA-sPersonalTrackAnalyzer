import json
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Load data
with open("RealResult.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

# Convert to DataFrame
df = pd.DataFrame(data)

# Extract year from timestamp
df['year'] = pd.to_datetime(df['ts']).dt.year

# List of features to analyze
features_to_analyze = ["danceability", "energy", "acousticness", "valence"]

# Calculate mean for each feature per year
mean_values = df.groupby('year')[features_to_analyze].mean()

# Visualize trends
for feature in features_to_analyze:
    plt.figure(figsize=(10, 6))
    plt.plot(mean_values.index, mean_values[feature], marker='o')
    plt.title(f'Mean {feature} Over the Years')
    plt.xlabel('Year')
    plt.ylabel(f'Mean {feature}')
    plt.show()

# Statistical analysis (t-test for simplicity)
for feature in features_to_analyze:
    print(f"T-test for {feature}:")
    years_to_compare = range(2018, 2024)  # Adjust the range of years as needed
    for year in years_to_compare:
        values = df[df['year'] == year][feature]
        values_other_year = df[df['year'] != year][feature]

        # Drop missing values
        values = values.dropna()
        values_other_year = values_other_year.dropna()

        # Check if there is variability in the data
        if values.var() > 0 and values_other_year.var() > 0:
            _, p_value = ttest_ind(values, values_other_year, equal_var=False)
            mean_difference = values.mean() - values_other_year.mean()

            significance_threshold = 0.05  # Adjust the significance threshold as needed
            if p_value < significance_threshold:
                print(f"  {year}: p-value = {p_value:.3e}, Mean Difference = {mean_difference:.3f} (significant)")
            else:
                print(f"  {year}: p-value = {p_value:.3e}, Mean Difference = {mean_difference:.3f} (not significant)")
        else:
            print(f"  {year}: Not enough variability in the data")

    print()
