import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
jwt = ""
source_dict = {}
base_url = 'http://127.0.0.1:5000'


def set_jwt(token):
    global jwt
    jwt = token


def get_jwt():
    return jwt


def get_dict():
    return source_dict


def set_dict(dct: dict):
    global source_dict
    source_dict = dct


