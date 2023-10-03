import requests
import json
import subprocess
from dataclasses import dataclass


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


def get_cheapest_fuel_location():
    url = "https://projectzerothree.info/api.php?format=json"
    page = requests.get(url)

    data = json.loads(page.text)
    best_prices = data.get("regions")[0].get("prices")

    selected_fuel_type = "U91"
    for fuel_type_best_price in best_prices:
        single_fuel_price = FuelPrice(**fuel_type_best_price)
        if selected_fuel_type == single_fuel_price.type:
            return single_fuel_price.gps


def get_rsd_connection_info():
    command = ["sudo", "python3", "-m", "pymobiledevice3", "remote", "start-quic-tunnel"]
    result = subprocess.run(command, capture_output=True, text=True)
    output = result.stdout

    prefix = "Use the follow connection option:"
    line = [line for line in output.splitlines() if line.startswith(prefix)][0]
    _, rsd_address, rsd_port = line.replace(prefix, "").split()

    return rsd_address, rsd_port


def simulate_location(gps_coords, rsd_info):
    rsd_address, rsd_port = rsd_info

    simulate_command = ["pymobiledevice3", "developer", "dvt", "simulate-location", "set", "--rsd", rsd_address, rsd_port, "--", str(gps_coords[0]), str(gps_coords[1])]

    subprocess.run(simulate_command)


def main():
    cheapest_fuel_location = get_cheapest_fuel_location()
    rsd_info = get_rsd_connection_info()
    simulate_location(cheapest_fuel_location, rsd_info)


if __name__ == "__main__":
    main()
