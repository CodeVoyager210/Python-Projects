from notification_manager import NotificationManager
def find_cheapest_flight(data,dest_name):
    if data is None or not data['data']:
        return  'N/A'
    lowest_price = float(data['data'][0]['price']['grandTotal'])
    for flight in data['data']:
        price = float(flight['price']['grandTotal'])
        if price < lowest_price:
            lowest_price = price
            send_notification = NotificationManager(lowest_price,dest_name)
    return lowest_price






