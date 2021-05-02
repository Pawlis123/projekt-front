from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import requests
from Views import widget, get_jwt


class CreateAccount(QDialog):
    def __init__(self):
        super(CreateAccount, self).__init__()
        loadUi("registerpage.ui", self)
        self.createAccountButton.clicked.connect(self.register_function)
        self.returnButton.clicked.connect(self.return_function)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repeatPassword.setEchoMode(QtWidgets.QLineEdit.Password)

    def register_function(self):
        username = self.username.text()
        password = self.password.text()
        confirm_password = self.repeatPassword.text()
        if password != confirm_password:
            print("wrooong")
            print(get_jwt())
        else:
            print("correct")

    def return_function(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)
