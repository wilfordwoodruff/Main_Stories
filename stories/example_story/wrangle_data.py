import pandas as pd
from download_data import load_data_into_dataframe  # Assuming the previous script is named download_data.py

def wrangle_data(df):
    # Perform data wrangling operations here
    # For example, let's drop any rows with missing values and rename a column
    df = df.dropna()
    df = df.rename(columns={"old_column_name": "new_column_name"})
    return df

if __name__ == "__main__":
    file = "derived_data.csv"  # Replace with your file name
    df = load_data_into_dataframe(file)
    df = wrangle_data(df)
    print(df)
