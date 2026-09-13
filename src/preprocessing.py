import pandas as pd 
import re 
from pathlib import Path 


src_dir = Path(__file__).resolve().parent


# === fitness dataframe preprocessing ===  
data_path = src_dir.parent / 'data' / 'raw' / 'gym_members_exercise_tracking.csv'
df = pd.read_csv(data_path)

# bringing the column names into a single & convenient style: 
def column_names_normalizer(df: pd.DataFrame) -> pd.DataFrame:  # ? -> utils.py 
    copied = df.copy()
    columns = copied.columns.to_list()
    
    lowercased = [col.lower() for col in columns]
    wo_incorrect_symbols = [re.sub(r'\W+', '_', col) for col in lowercased]
    normalized = [re.sub(r'_+', '_', col.strip('_')) for col in wo_incorrect_symbols]
        
    copied = copied.rename(columns=dict(zip(columns, normalized)))
    return copied 
    
    
fitness_df = column_names_normalizer(df)
print(fitness_df.columns)

# converting height from meters to centimeters
fitness_df.height_m = fitness_df.height_m * 100 
fitness_df = fitness_df.rename(columns={'height_m': 'height_cm'})

# saving the prepared dataset in data/processed/: 
fitness_df.to_csv(src_dir.parent / 'data' / 'processed' / 'fitness_df.csv', index=False)