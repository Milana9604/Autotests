import requests
import json

class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru/'

    def get_api_key(self, email, password):

        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key, filter):
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}
        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_new_pet(self, auth_key):
        form_data = {'name':'Abba','animal_type':'cat','age':'41'}
        headers = {'auth_key': auth_key['key'], 'accept': 'application/json', 'Content-Type': 'multipart/form-data'}
        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=form_data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result