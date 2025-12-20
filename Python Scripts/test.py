import requests
import csv
from io import StringIO
# https://health.data.ny.gov/resource/cnih-y5dw.csv

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

url = "https://health.data.ny.gov/resource/cnih-y5dw.csv?$limit=50000"
csv_text = fetch_data(url)
reader = csv.DictReader(StringIO(csv_text))
print(reader.fieldnames)

rows = list(reader)
print("Total rows:", len(rows))