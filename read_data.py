import pandas as pd

def read_data_from_url(url):
    df = pd.read_csv(url)
    return df

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/wilfordwoodruff/Main-Data/main/data/derived/derived_data.csv"
    df = read_data_from_url(url)
    print(df)
