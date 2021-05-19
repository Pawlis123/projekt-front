from Views import get_jwt
import requests


def article_fetch():
    header = {'Authorization': 'Bearer ' + get_jwt().strip()}
    articles = requests.get('http://127.0.0.1:5000/api/articles', headers=header)
    articles_dict = articles.json()
    if 'msg' in articles_dict:
        return {}
    return articles_dict
