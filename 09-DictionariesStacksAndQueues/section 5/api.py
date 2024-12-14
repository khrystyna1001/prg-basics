import requests
import json
from datetime import datetime

url = "https://api.nbp.pl/api/exchangerates/rates/a/eur/last/10/?format=json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Parse the JSON response into a Python dictionary
    with open("euro.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print("Data has been saved to euro.json")
else:
    print("Failed to fetch data from the API. Status code:", response.status_code)

try:
    with open("euro.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    print(f"{'Date':<15}{'Number':<15}{'MID':<15}")
    print("="*50)

    for rate in data['rates']:
        date = rate['effectiveDate']
        num = rate['no']  
        mid = rate['mid']  

        print(f"{date:<15}{num:<15}{mid:<15}")
        
except FileNotFoundError:
    print("euro.json file not found. Please make sure the data was saved correctly.")