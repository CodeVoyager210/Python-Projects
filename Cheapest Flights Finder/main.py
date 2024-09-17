from data_manager import DataManager
from flight_search  import FlightSearch
from datetime import datetime,timedelta
from flight_data import find_cheapest_flight
flight_search = FlightSearch()
data = DataManager()
sheet_data = data.json['prices']
origin_city = 'LON'
city = 'London'
tomorrow = datetime.now() + timedelta(days=1)
after_6_months = datetime.now() + timedelta(days=(6 * 30))
if sheet_data[0]['iataCode'] == '':
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'].upper())
    data.update_sheet()
for destination in sheet_data:
    flights = flight_search.check_flights(origin_city=origin_city,dest_city=destination['iataCode'],from_time=tomorrow,to_time=after_6_months)
    destination_name = destination['city']
    cheapest_flight = find_cheapest_flight(flights,destination_name)
    print(f"{destination_name}: £{cheapest_flight}")
    if cheapest_flight == 'N/A' :
        print(f'No direct flight found in {destination['city']}. Checking for indirect flights...')
        stopover_flights = flight_search.check_flights(origin_city=origin_city,dest_city=destination['iataCode'],from_time=tomorrow,to_time=after_6_months,is_direct=False)
        cheapest_flight = find_cheapest_flight(flights,destination_name)
        print(f'Cheapest indirect flight for {destination_name} is : £{cheapest_flight}')



