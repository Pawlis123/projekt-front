from Views import get_jwt, base_url
import requests


def article_fetch():
    header = {'Authorization': 'Bearer ' + get_jwt().strip()}
    try:
        articles = requests.get(base_url+'/api/articles', headers=header)
    except:
        return "Internal server error."
    articles_dict = articles.json()
    if 'msg' in articles_dict:
        return {}
    return articles_dict
