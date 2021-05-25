from Views import get_jwt, base_url
import requests


def url_edit(urls: dict):
    header = {'Authorization': 'Bearer ' + get_jwt().strip()}
    response = requests.post(base_url + '/api/add-urls', json=urls, headers=header)
    return response.json()['msg']


def url_delete(key: str):
    header = {'Authorization': 'Bearer ' + get_jwt().strip()}
    response = requests.post(base_url + '/api/delete-url/{}'.format(key), headers=header)
    return response.json()['msg']
