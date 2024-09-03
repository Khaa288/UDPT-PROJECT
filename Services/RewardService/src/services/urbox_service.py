import requests

class UrboxService():
    url: str

    def __init__(self):
        self.url = ''

    def list_gifts():
        url = 'https://api.urbox.vn/2.0/gift/getlist'
        response = requests.get(url)
        data = response.json()

        print(data)
        return data['data']['items']
    
    def get_gift_by_id(gift_id):
        url = 'https://api.urbox.vn/2.0/gift/item'

        body = {'id': gift_id}

        response = requests.post(url, json=body)
        data = response.json()

        if (data['done'] == 0):
            return None
        return data

