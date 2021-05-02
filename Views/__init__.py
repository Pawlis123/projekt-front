import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
jwt = ""


def set_jwt(token):
    global jwt
    jwt = token

def get_jwt():
    return jwt
