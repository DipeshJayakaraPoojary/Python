import os
import pandas as pd


INPUT_FOLDER = "data_files"


SUPPORTED_EXTENSIONS = ('.csv', '.xlsx', '.xls', '.json')

def clean_dataframe(df):
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df.dropna(axis=0, how='all', inplace=True)  
    df.dropna(axis=1, how='all', inplace=True) 
    df.fillna('', inplace=True)  
    return df

def read_file(filepath):
    _, ext = os.path.splitext(filepath) # Get file extension
    try:
        if ext == '.csv':
            return pd.read_csv(filepath)
        elif ext in ['.xlsx', '.xls']:
            return pd.read_excel(filepath)
        elif ext == '.json':
            return pd.read_json(filepath)
    except Exception as e:
        print(f"Failed to read {filepath}: {e}")
        return None

def ingest_and_merge(folder_path):
    all_dfs = []

    for filename in os.listdir(folder_path):
        if filename.endswith(SUPPORTED_EXTENSIONS):
            full_path = os.path.join(folder_path, filename)
            print(f"Processing: {full_path}")
            df = read_file(full_path)
            if df is not None:
                df = clean_dataframe(df)
                df['source_file'] = filename 
                all_dfs.append(df)

    if all_dfs:
        merged_df = pd.concat(all_dfs, ignore_index=True)
        print(f"Total rows merged: {merged_df.shape[0]}")
        return merged_df
    else:
        print("No valid files found.")
        return pd.DataFrame()

if __name__ == "__main__":
    merged_data = ingest_and_merge(INPUT_FOLDER)
    merged_data.to_csv("merged_output.csv", index=False)
    print("Merged data saved to 'merged_output.csv'")
