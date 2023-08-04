import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer
import os

# Read the CSV file and get the relevant columns
csv_file = "vulnerabilities.csv"
columns_to_process = ['BugType', 'Company', 'Reporter', 'BugSeverity', 'Acquisition', 'Reward', 'Authenticated', 'ToolUsed']
target = pd.read_csv(csv_file, usecols=columns_to_process)

# Filter bad records (like NaN) from the file, so it can be processed
target = target.dropna()

# Function to convert continuous values to discrete bins
def convert_to_discrete(col):
    if pd.api.types.is_numeric_dtype(target[col]):
        if target[col].nunique() <= 5:
            return target[col].astype(str)
        else:
            # Define your own binning criteria here
            # For simplicity, we'll use 3 bins - Low, Medium, High
            bin_labels = ['Low', 'Medium', 'High']
            bin_edges = [target[col].min(), target[col].quantile(1/3), target[col].quantile(2/3), target[col].max()]
            return pd.cut(target[col], bins=bin_edges, labels=bin_labels, include_lowest=True)
    else:
        return target[col]

# Apply the convert_to_discrete function to all columns
for col in columns_to_process:
    target[col] = convert_to_discrete(col)

# Output the updated DataFrame with discrete values to a new CSV file
output_csv = "vulnerabilities_discrete.csv"
target.head(200000).to_csv(output_csv, index=False)

print(f"Data with discrete values saved to '{output_csv}'.")

