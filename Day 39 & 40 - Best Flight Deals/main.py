from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "YYC"

# check if sheet_data contains any values for the "iataCode" key.
# If not, pass each city name in sheet_data one-by-one to the FlightSearch class to get the corresponding IATA code
# for that city using the Flight Search API.

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# check flight to all the cities listed in your google sheet
for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    # if the price is lower tan your limit, send a text message to your phone
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} "
                    f"to {flight.destination_city}-{flight.destination_airport}, "
                    f"from {flight.out_date} to {flight.return_date}."
        )
        # print(f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} "
        #       f"to {flight.destination_city}-{flight.destination_airport}, "
        #       f"from {flight.out_date} to {flight.return_date}.")