import requests
class DataManager:
    def __init__(self):
        self.website = 'https://api.sheety.co/a84469e42be5cba1039cd8534bcbb833/dealsFlight/prices'
        self.website_2 = 'https://api.sheety.co/a84469e42be5cba1039cd8534bcbb833/users/sheet1'
        request = requests.get(url=self.website)
        self.json = request.json()
    def update_sheet(self):
        for sh in self.json['prices']:
            updated_data = {
                'price' : {
                    'iataCode' : sh['iataCode']
                }
            }
            put = requests.put(url=f'{self.website}/{sh['id']}',json=updated_data)
    def get_customer_emails(self):
        response = requests.get(url=self.website_2)
        return response.json()



