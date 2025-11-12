import os
import pandas as pd

path = "data/raw/"
path_res = "data/CSV_renamed/"

os.makedirs(path_res, exist_ok=True)

vars_df = pd.read_csv('data/extra/variables.csv')

#convert all .xpt files in the directory to .csv files and move it to the CSV folder

for filename in os.listdir(path):
    if filename.endswith(".XPT"):
        xpt_file = os.path.join(path, filename)
        csv_file = os.path.join(path_res, filename.replace(".XPT", ".csv"))
        
        # Read the .xpt file and convert to .csv
        df = pd.read_sas(xpt_file, format='xport')
        
        # Rename columns
        base_name = filename.replace('.XPT', '')
        file_vars = vars_df[vars_df['Data File Name'] == base_name]
        rename_dict = dict(zip(file_vars['Variable Name'], file_vars['Renamed_variables']))
        df.rename(columns=rename_dict, inplace=True)
        
        # Remove existing file if it exists
        if os.path.exists(csv_file):
            os.remove(csv_file)
        
        df.to_csv(csv_file, index=False)
        
        print(f"Converted {filename} to {csv_file}")