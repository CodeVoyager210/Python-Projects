import requests
import smtplib
from datetime import datetime
import time
def check_loc():
    global iss_to_location
    if close_lat_position and close_long_position:
        if time_now.hour == sunrise or time_now.hour == sunset:
            iss_to_location = True


MY_LAT = 38.242253
MY_LONG = 21.735909
count = 0
while True:
    count = 0
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    close_lat_position = MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
    close_long_position = MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    iss_to_location = False
    if iss_to_location:
        connection = smtplib.SMTP('smpt.mail.com')
        connection.starttls()
        connection.login(user='your_email', password='your_password')
        connection.sendmail(from_addr='your_email', to_addrs='your_email',
                            msg='Subject:ISS Near Your Location \n\n\Go outside and look')
        connection.close()
        break
    else:
        while count < 60:
            count +=1
            time.sleep(1)






