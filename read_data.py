import requests
import pandas as pd

def download_file_from_github(user, repo, file):
    url = f"https://raw.githubusercontent.com/{user}/{repo}/main/{file}"
    response = requests.get(url)
    response.raise_for_status()  # Ensure we got a successful response

    with open(file, 'wb') as f:
        f.write(response.content)

    print(f"Downloaded {file} from {user}/{repo}")

def load_data_into_dataframe(file):
    df = pd.read_csv(file)
    return df

if __name__ == "__main__":
    user = "tylerenglish"  # Replace with your GitHub username
    repo = "Main-Data"  # Replace with your repository name
    file = "derived_data.csv"  # Replace with your file name

    download_file_from_github(user, repo, file)
    df = load_data_into_dataframe(file)
