import pandas as pd
import os
from pathlib import Path

# Get all CSV files from data/CSV directory
csv_dir = Path("data/CSV")
csv_files = sorted(csv_dir.glob("*.csv"))

print(f"Found {len(csv_files)} CSV files to join")

# Load the first CSV file
first_file = csv_files[0]
print(f"Starting with: {first_file.name}")
df_combined = pd.read_csv(first_file)

# Join all other CSV files
for csv_file in csv_files[1:]:
    print(f"Joining: {csv_file.name}")
    df_temp = pd.read_csv(csv_file)
    df_combined = df_combined.merge(df_temp, on="sequence_no", how="outer")

print(f"\nCombined shape: {df_combined.shape}")
print(f"Total columns: {df_combined.shape[1]}")
print(f"Total rows: {df_combined.shape[0]}")

# Save the combined file
output_path = "data/combined_data.csv"
df_combined.to_csv(output_path, index=False)
print(f"\nCombined data saved to: {output_path}")

# Display summary
print("\nColumn summary:")
print(f"Columns: {list(df_combined.columns)[:10]}... (showing first 10)")
print(f"\nData types:\n{df_combined.dtypes.value_counts()}")
