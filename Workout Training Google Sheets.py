import requests
from datetime import datetime
APP_ID = 'a3fc9ced'
APP_KEY = 'dd3ccc74d8ae0327098e860c7aa7f0bd'
website_exercise = 'https://trackapi.nutritionix.com/v2/natural/exercise'
website_authentication = 'developer.nutritionix.com'
date = datetime.now()
user_input = input('Tell me which exercises you did: ')
authentication_header = {
    'x-app-id' : APP_ID,
    'x-app-key' : APP_KEY
}
exercise_params = {
    'query' : user_input
}
response = requests.post(url=website_exercise,json=exercise_params,headers=authentication_header)
exercise_data = response.json()
for exercise in exercise_data['exercises']:
    exercise_name = exercise['name']
    exercise_duration = exercise['duration_min']
    exercise_calories = exercise['nf_calories']
    google_sheets_api = 'https://api.sheety.co/a84469e42be5cba1039cd8534bcbb833/workout/workouts'
    google_sheets_params = {
        'workout': {
            'date': date.strftime('%d/%m/%Y'),
            'time': date.strftime('%X'),
            'exercise': exercise_name.title(),
            'duration': exercise_duration,
            'calories': exercise_calories
        }
    }
    response_sheets = requests.post(url=google_sheets_api, json=google_sheets_params)
input('Exercises saved to google sheets! Press any key to close the program')