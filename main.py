#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

#Creating Objects
flightSearch = FlightSearch()
dataManager = DataManager()
flightData = FlightData()
notifications = NotificationManager()

sheet_data_list = dataManager.get_sheet_data()
email_list = dataManager.get_customer_emails_list()
for row in sheet_data_list:

    # For inserting iata code into google sheet
    if row["iataCode"] == "":
        city = row['city']
        iata_code = flightSearch.get_iata_code(city)
        row_id = row['id']
        dataManager.update_sheet_iata_code(row_id=row_id, iata_code=iata_code)

    # Searching cheapest flight
    _iata_code = row['iataCode']
    lowest_price = row['lowestPrice']
    flight_detail = flightSearch.cheapest_flight_check(to_city_iata_code=_iata_code, max_price=lowest_price)

    # Direct Flight
    if flight_detail['meta']['count'] > 0:
        alert_message = flightData.structure_flight_data(flight_detail)
        # notifications.send_alert(alert_message)
        notifications.send_mails(email_list, alert_message)

    # Indirect Flight
    else:
        flight_detail = flightSearch.cheapest_flight_check(to_city_iata_code=_iata_code, max_price=lowest_price,
                                                           is_direct=False)
        if flight_detail['meta']['count'] > 0:
            alert_message = flightData.structure_flight_data(flight_detail)
            # notifications.send_alert(alert_message)
            notifications.send_mails(email_list, alert_message)


