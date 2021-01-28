import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/e074014c1c4c8da5f6d47acc268ed697/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    # Use the Sheety API to GET all the data in that sheet and print it out
    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    # use the row id  from sheet_data to update the Google Sheet with the IATA codes.
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
