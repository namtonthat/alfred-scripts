# %%
from bs4 import BeautifulSoup
import requests
import clipboard

# %%
url = "https://projectzerothree.info/prices.php"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

## Only return the table of best prices within Australia
best_prices = soup.tbody.find_all("tr")

prices = {}
for i in range(0, len(best_prices)):
    price_info = best_prices[i].find_all("td")
    fuel_type = price_info[0].text
    price = price_info[1].text
    location_list = [i.text for i in price_info[3:6]]
    location = " ".join(location_list)
    prices[fuel_type] = [price, location]

## To call another fuel type - return prices.get('fuelType')
## Available fuelTypes are
## E10, U91, U98, Diesel, LPG

cheapest_fuel = prices.get("U91")[1]

clipboard.copy(cheapest_fuel)
print(cheapest_fuel)
