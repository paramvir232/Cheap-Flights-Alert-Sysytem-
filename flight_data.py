class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.stops = 0
    def structure_flight_data(self, flight_data):
        """ Formatting the output data in readable manner"""

        data = flight_data['data'][0]
        ticket_price = data['price']['total']

        location = data['itineraries'][0]['segments']

        # location_list =[item['departure']['iataCode'] for item in data['itineraries'][0]['segments']]
        _from = location[0]['departure']['iataCode']
        _to = location[len(location)-1]['arrival']['iataCode']
        # print(location_list)

        dates = [(item['segments'][0]['departure']['at']).split('T')[0] for item in data['itineraries']]
        departure_date = dates[0]
        return_date = dates[1]
        self.stops = len(data['itineraries'][0]['segments'])
        structured_data = f'\nLow price Alert!! Only €{ticket_price} to\nfly from {_from} to {_to} on\n{departure_date} until {return_date}\n with {self.stops} stops.'

        return structured_data
