from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import requests
from Views import widget


class CreateAccount(QDialog):
    def __init__(self):
        super(CreateAccount, self).__init__()
        loadUi("registerpage.ui", self)
        self.createAccountButton.setStyleSheet(open("buttons.qss", "r").read())
        self.returnButton.setStyleSheet(open("buttons.qss", "r").read())
        self.createAccountButton.clicked.connect(self.register_function)
        self.returnButton.clicked.connect(self.return_function)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repeatPassword.setEchoMode(QtWidgets.QLineEdit.Password)

    def register_function(self):
        username = self.username.text()
        password = self.password.text()
        confirm_password = self.repeatPassword.text()
        if len(password) < 6:
            self.errorLabel.setText("Password should be at least 6 characters long")
            self.password.setText("")
            self.repeatPassword.setText("")
        elif password != confirm_password:
            self.errorLabel.setText("Passwords are not equal.")
            self.password.setText("")
            self.repeatPassword.setText("")
        else:
            try:
                user_obj = {'username': username, 'password': password}
                msg = requests.post('http://127.0.0.1:5000/api/register', json=user_obj).json()
                self.errorLabel.setText(msg['msg'])
                self.username.setText("")
                self.password.setText("")
                self.repeatPassword.setText("")
            except Exception as e:
                self.errorLabel.setText('No internet connection')


    def return_function(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)
        widget.removeWidget(self)
