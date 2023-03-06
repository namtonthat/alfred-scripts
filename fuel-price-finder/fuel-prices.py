# %%
import requests
import clipboard
from dataclasses import dataclass
import json


@dataclass
class FuelPrice:
    """Class to hold Fuel Price data"""

    state: str
    postcode: str
    price: float
    suburb: str
    name: str
    lat: float
    lng: float
    type: str

    @property
    def location(self):
        return f"{self.suburb}, {self.state} {self.postcode}, Australia"

    @property
    def gps(self):
        return (self.lat, self.lng)


# %%
url = "https://projectzerothree.info/api.php?format=json"
page = requests.get(url)

data = json.loads(page.text)
best_prices = data.get("regions")[0].get("prices")

## Only return the table of best prices within Australia
selected_fuel_type = "U91"
for fuel_type_best_price in best_prices:
    single_fuel_price = FuelPrice(**fuel_type_best_price)
    if selected_fuel_type == single_fuel_price.type:
        cheapest_fuel = single_fuel_price.location

clipboard.copy(cheapest_fuel)
print(single_fuel_price.location)
