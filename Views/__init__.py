import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
jwt = ""
source_dict = {}


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


def add_entries(new_values: dict):
    for entry in new_values.items():
        if not source_dict[entry[0]]:
            source_dict[entry[0]] = entry[1]
