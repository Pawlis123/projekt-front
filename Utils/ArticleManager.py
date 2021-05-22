from Views import get_jwt
import requests


def url_edit(urls: dict):
    header = {'Authorization': 'Bearer ' + get_jwt().strip()}
    response = requests.post('http://127.0.0.1:5000/api/add-urls', json=urls, headers=header)
    return response.json()['msg']


def url_delete(key: str):
    header = {'Authorization': 'Bearer ' + get_jwt().strip()}
    response = requests.post('http://127.0.0.1:5000/api/delete-url/{}'.format(key), headers=header)
    return response.json()['msg']
