import pandas as pd

def read_data_from_url(url):
    df = pd.read_csv(url)
    return df

def wrangle_data(df):
    # Perform data wrangling operations here
    # For example, let's drop any rows with missing values and rename a column
    df = df.dropna()
    df = df.rename(columns={"old_column_name": "new_column_name"})
    return df

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/wilfordwoodruff/Main-Data/main/data/derived/derived_data.csv"
    df = read_data_from_url(url)
    df = wrangle_data(df)
    print(df)

