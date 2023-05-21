import pandas as pd

# Load the messy FIFA 21 raw data from a CSV file
data = pd.read_csv("fifa21_raw_data.csv")

# Display the first few rows of the data
print("Original Data:")
print(data.head())

# Drop unnecessary columns
columns_to_drop = ["Column1", "Column2"]
data.drop(columns_to_drop, axis=1, inplace=True)

# Rename columns
column_mapping = {
    "OldColumnName1": "NewColumnName1",
    "OldColumnName2": "NewColumnName2"
}
data.rename(columns=column_mapping, inplace=True)

# Convert data types
data["NumericColumn"] = pd.to_numeric(data["NumericColumn"], errors="coerce")

# Handle missing values
data["CategoricalColumn"].fillna("Unknown", inplace=True)
data["NumericColumn"].fillna(data["NumericColumn"].mean(), inplace=True)

# Apply transformations to columns
data["CategoricalColumn"] = data["CategoricalColumn"].str.lower()
data["StringColumn"] = data["StringColumn"].str.strip()

# Perform data filtering
filtered_data = data[data["NumericColumn"] > 0]

# Perform data aggregation
aggregated_data = data.groupby("CategoryColumn")["NumericColumn"].sum().reset_index()

# Sort the data
sorted_data = data.sort_values("NumericColumn", ascending=False)

# Save the cleaned and transformed data to a new CSV file
sorted_data.to_csv("fifa21_cleaned_data.csv", index=False)

# Display the cleaned and transformed data
print("Cleaned and Transformed Data:")
print(sorted_data.head())